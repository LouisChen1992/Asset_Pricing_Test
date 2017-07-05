import csv
import numpy as np
from scipy.stats import chi2, norm

def load_data(path, start_row, end_row):
	with open(path, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		cur_row = 0
		data = []
		for row in reader:
			cur_row += 1
			if cur_row < start_row:
				continue
			data.append([float(element) for element in row[1:]])
			if cur_row == end_row:
				break
	return np.array(data).T

def test_statistic(F, Y, T, N, Q):
	"""Test statistic for time-series regression

	Args: 
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors

	Returns: 
		Lambda: Test statistic
		SD: Standard deviation
		CV: Confidence interval
		p_value: P-value
	"""

	y = 1.0 * N / T
	X = np.concatenate((np.ones((1,T)),F), axis = 0)
	B_hat = np.dot(np.dot(Y, np.transpose(X)), np.linalg.inv(np.dot(X, np.transpose(X))))
	alpha_hat = B_hat[:,0]
	Sigma_hat = (np.dot(Y, np.transpose(Y)) - np.dot(np.dot(B_hat, X), np.transpose(Y))) / T
	k = T - np.dot(np.sum(F, axis = 1), np.dot(np.linalg.inv(np.dot(F, np.transpose(F))), np.sum(F, axis = 1)))

	Lambda = 1.0 * (T - N - Q) / T / N * k * np.dot(alpha_hat, np.dot(np.linalg.inv(Sigma_hat), alpha_hat)) # test statistic
	SD = np.sqrt(2.0 / (1 - y) / N) # standard error
	CV = (Lambda - 1) / SD # critical value
	p_value = 1 - norm.cdf(CV) # p-value
	return (Lambda, SD, CV, p_value)

def test_statistic_cross(F, Y, T, N, Q):
	"""Test statistic for cross-sectional regression

	Args: 
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors

	Returns: 
		Lambda: Test statistic
		SD: Standard deviation
		CV: Confidence interval
		p_value: P-value
	"""

	y = 1.0 * N / T
	X = np.concatenate((np.ones((1,T)),F), axis = 0)
	B_hat = np.dot(np.dot(Y, np.transpose(X)), np.linalg.inv(np.dot(X, np.transpose(X))))
	beta = B_hat[:,1:]
	P1 = np.identity(T) - np.dot(np.dot(np.transpose(F), np.linalg.pinv(np.dot(F, np.transpose(F)))), F)
	P2 = np.identity(N) - np.dot(beta, np.dot(np.linalg.pinv(np.dot(np.transpose(beta), beta)), np.transpose(beta)))
	Sigma = np.dot(Y, np.dot(P1, np.transpose(Y))) / T
	alpha = np.dot(P2, np.sum(Y, axis = 1) / T)
	cov = np.dot(np.dot(P2, Sigma),P2) / T
	F_bar = np.sum(F, axis = 1) / T
	k = (1 - np.dot(F_bar, np.dot(np.linalg.pinv(np.dot(F, np.transpose(F)) / T), F_bar))) * T
	Lambda = np.dot(alpha, np.dot(np.linalg.pinv(cov), alpha)) * (T - Q) * k / (N - Q) / T / T
	SD = np.sqrt(2.0 * (1 - y) / (N - Q)) # standard error
	CV = (Lambda - 1) / SD # critical value
	p_value = 1 - norm.cdf(CV) # p-value
	return (Lambda, SD, CV, p_value)

def result(F, Y, T, N, Q):
	Lambda, SD, CV, p_value = test_statistic(F, Y, T, N, Q) # Our test statistic
	Lambda_1 = 1.0 * T / (T - N - Q) * N * Lambda # test statistic 1
	p_value_1 = 1 - chi2.cdf(Lambda_1, N)
	Lambda_2 = N * Lambda # test statistic 2
	p_value_2 = 1 - chi2.cdf(Lambda_2, N)
	return (Lambda, p_value, Lambda_1, p_value_1, Lambda_2, p_value_2)

def result_cross(F, Y, T, N, Q):
	Lambda, SD, CV, p_value = test_statistic_cross(F, Y, T, N, Q)
	Lambda_1 = (N - Q) * Lambda
	p_value_1 = 1 - chi2.cdf(Lambda_1, N - Q)
	return (Lambda, p_value, Lambda_1, p_value_1)

def display(result, message, N, T, f = None, Factors = None):
	if f is None:
		print '%' * 80
		print '    %d Portfolios Fama-French Model: N = %d, T = %d' % (N, N, T)
		print '    Use %s Data From %s To %s. ' % (message[0], message[1], message[2])
		if Factors is not None:
			print '    Test On %d Factors: %s. \n' % (len(Factors), ', '.join(Factors))
		print '{:>20}  {:>20}  {:>20}'.format('Test Statistic', 'Estimation', 'p-value')
		print '{:>20}  {:>20}  {:>20}'.format('Lambda', str(result[0]), str(result[1]))
		print '{:>20}  {:>20}  {:>20}'.format('Lambda_1', str(result[2]), str(result[3]))
		print '{:>20}  {:>20}  {:>20}'.format('Lambda_2', str(result[4]), str(result[5]))
		print '\n' + '%' * 80 + '\n'
	else:
		f.write('%' * 80 + '\n')
		f.write('    %d Portfolios Fama-French Model: N = %d, T = %d\n' % (N, N, T))
		f.write('    Use %s Data From %s To %s. \n' % (message[0], message[1], message[2]))
		if Factors is not None:
			f.write('    Test On %d Factors: %s. \n\n' % (len(Factors), ', '.join(Factors)))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Test Statistic', 'Estimation', 'p-value'))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Lambda', str(result[0]), str(result[1])))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Lambda_1', str(result[2]), str(result[3])))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Lambda_2', str(result[4]), str(result[5])))
		f.write('\n' + '%' * 80 + '\n\n')

def display_cross(result, message, N, T, f = None, Factors = None):
	if f is None:
		print '%' * 80
		print '    %d Portfolios Fama-French Model: N = %d, T = %d' % (N, N, T)
		print '    Use %s Data From %s To %s. ' % (message[0], message[1], message[2])
		if Factors is not None:
			print '    Test On %d Factors: %s. \n' % (len(Factors), ', '.join(Factors))
		print '{:>20}  {:>20}  {:>20}'.format('Test Statistic', 'Estimation', 'p-value')
		print '{:>20}  {:>20}  {:>20}'.format('Lambda', str(result[0]), str(result[1]))
		print '{:>20}  {:>20}  {:>20}'.format('Lambda_1', str(result[2]), str(result[3]))
		print '\n' + '%' * 80 + '\n'
	else:
		f.write('%' * 80 + '\n')
		f.write('    %d Portfolios Fama-French Model: N = %d, T = %d\n' % (N, N, T))
		f.write('    Use %s Data From %s To %s. \n' % (message[0], message[1], message[2]))
		if Factors is not None:
			f.write('    Test On %d Factors: %s. \n\n' % (len(Factors), ', '.join(Factors)))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Test Statistic', 'Estimation', 'p-value'))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Lambda', str(result[0]), str(result[1])))
		f.write('{:>20}  {:>20}  {:>20}\n'.format('Lambda_1', str(result[2]), str(result[3])))
		f.write('\n' + '%' * 80 + '\n\n')