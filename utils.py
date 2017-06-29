import numpy as np

def data_generation(beta, mu, sigma, N, T, Q, A, B):
	"""Generates data using formula: Y = beta * F + E

	Args: 
		beta: An N * Q matrix representing factor loadings
		mu: A list of length Q containing the means of Q factors
		sigma: A list of length Q containing the standard deviations of Q factors
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors
		A: An N * N matrix representing cross-sectional correlation of idiosyncratic errors
		B: A T * T matrix representing time-series correlation of idiosyncratic errors

	Returns:
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
	"""

	F = np.concatenate([np.random.normal(loc = mu[i], scale = sigma[i], size = (1,T)) for i in xrange(Q)], axis = 0)
	E = np.dot(np.dot(A, np.random.normal(loc = 0, scale = 0.1, size = (N, T))), B)
	Y = np.dot(beta, F) + E
	return (F, Y)

def test_statistic_TR(F, Y, N, T, Q, B_est = None):
	"""Test statistic for time-series regression

	Args: 
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors
		B_est: A T * T matrix representing estimation of time-series correlation of idiosyncratic errors 

	Returns: 
		Lambda: Test statistic
	"""

	X = np.concatenate((np.ones((1,T)),F), axis = 0)
	R = Y
	if B_est is not None:
		X = X.dot(np.linalg.pinv(B_est))
		R = R.dot(np.linalg.pinv(B_est))
	B_hat = np.dot(np.dot(R, np.transpose(X)), np.linalg.inv(np.dot(X, np.transpose(X))))
	alpha_hat = B_hat[:,0]
	Sigma_hat = (np.dot(R, np.transpose(R)) - np.dot(np.dot(B_hat, X), np.transpose(R))) / T
	if B_est is not None:
		F_tilde = X[1:]
		eta = X[0]
		k = eta.dot(eta) - np.dot(F_tilde.dot(eta), np.dot(np.linalg.inv(F_tilde.dot(F_tilde.T)), F_tilde.dot(eta)))
	else:
		k = T - np.dot(np.sum(F, axis = 1), np.dot(np.linalg.inv(np.dot(F, np.transpose(F))), np.sum(F, axis = 1)))
	Lambda = 1.0 * (T - N - Q) / T / N * k * np.dot(alpha_hat, np.dot(np.linalg.pinv(Sigma_hat), alpha_hat))
	return Lambda

def test_statistic_CR_beta(beta, F, Y, N, T, Q, B_est = None):
	"""Test statistic for cross-sectional regression with beta given

	Args: 
		beta: An N * Q matrix representing factor loadings
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors
		B_est: A T * T matrix representing estimation of time-series correlation of idiosyncratic errors 

	Returns: 
		Lambda: Test statistic
	"""

	P = np.identity(N) - np.dot(beta, np.dot(np.linalg.inv(np.dot(np.transpose(beta), beta)), np.transpose(beta)))
	if B_est is not None:
		R = Y.dot(np.linalg.pinv(B_est))
		F_tilde = F.dot(np.linalg.pinv(B_est))
		eta = np.dot(np.ones(T), np.linalg.pinv(B_est))
	else:
		R = Y
		F_tilde = F
		eta = np.ones(T)
	alpha = np.dot(P, R.dot(eta)) / eta.dot(eta)
	E = R - np.dot(beta, F_tilde)
	Sigma = np.dot(E, np.transpose(E)) / T
	cov = np.dot(np.dot(P, Sigma),P) / T
	Lambda = np.dot(alpha, np.dot(np.linalg.pinv(cov), alpha)) / (N - Q) / T * eta.dot(eta)
	return Lambda

def test_statistic_CR_intercept(F, Y, N, T, Q, B_est = None):
	"""Test statistic for cross-sectional regression

	Args: 
		F: A Q * T matrix representing factors
		Y: An N * T matrix representing asset returns
		N: Number of assets
		T: Number of (time) observations
		Q: Number of factors
		B_est: A T * T matrix representing estimation of time-series correlation of idiosyncratic errors 

	Returns: 
		Lambda: Test statistic
	"""

	X = np.concatenate((np.ones((1,T)),F), axis = 0)
	if B_est is not None:
		X = X.dot(np.linalg.pinv(B_est))
		F_tilde = X[1:]
		eta = X[0]
		R = Y.dot(np.linalg.pinv(B_est))
		k = eta.dot(eta) - np.dot(F_tilde.dot(eta), np.dot(np.linalg.inv(F_tilde.dot(F_tilde.T)), F_tilde.dot(eta)))
	else:
		F_tilde = F
		eta = np.ones(T)
		R = Y
		k = T - np.dot(np.sum(F, axis = 1), np.dot(np.linalg.inv(np.dot(F, np.transpose(F))), np.sum(F, axis = 1)))

	B_hat = np.dot(np.dot(R, np.transpose(X)), np.linalg.inv(np.dot(X, np.transpose(X))))
	beta = B_hat[:,1:]

	P1 = np.identity(T) - np.dot(np.dot(np.transpose(F_tilde), np.linalg.pinv(np.dot(F_tilde, np.transpose(F_tilde)))), F_tilde)
	P2 = np.identity(N) - np.dot(beta, np.dot(np.linalg.pinv(np.dot(np.transpose(beta), beta)), np.transpose(beta)))
	Sigma = np.dot(R, np.dot(P1, np.transpose(R))) / T
	alpha = np.dot(P2, R.dot(eta)) / eta.dot(eta)
	cov = np.dot(np.dot(P2, Sigma),P2) / T
	
	Lambda = np.dot(alpha, np.dot(np.linalg.pinv(cov), alpha)) * (T - Q) * k / (N - Q) / T / T
	return Lambda