import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from utils import *
from matplotlib import rc
from scipy.stats import chi2

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--N', help = 'Number of Assets')
parser.add_argument('-t', '--T', help = 'Time')
parser.add_argument('-q', '--Q', help = 'Number of Factors')
parser.add_argument('-e', '--E', help = 'Idiosyncratic Errors')
args = parser.parse_args()

N = int(args.N)
T = int(args.T)
Q = int(args.Q)
y = 1.0 * N / T

### parameters for factors 
sigma = np.linspace(0.05, 0.15, num = 3)
mu = sigma * 0.5
### number of experiments
K = 5000

beta = np.random.normal(size = (N, Q))
if args.E == '1': 
	A = np.identity(N)
	B = np.identity(T)
elif args.E == '2':
	rho = 0.5
	Sigma = np.identity(N) + np.diag([rho]*(N-1), 1) + np.diag([rho]*(N-1), -1)
	A = np.linalg.cholesky(Sigma)
	B = np.identity(T)
elif args.E == '3':
	rho = 0.5
	q = 0.1
	Sigma = np.identity(N) + np.diag([rho]*(N-1), 1) + np.diag([rho]*(N-1), -1)
	A = np.linalg.cholesky(Sigma)
	B = np.identity(T) + np.diag([q]*(T-1),1)

Lambda = np.zeros((3,K))
for i in xrange(K):
	F, Y = data_generation(beta, mu, sigma, N, T, Q, A, B)
	if args.E == '3':
		Lambda[0,i] = test_statistic_TR(F, Y, N, T, Q, B)
		Lambda[1,i] = test_statistic_CR_beta(beta, F, Y, N, T, Q, B)
		Lambda[2,i] = test_statistic_CR_intercept(F, Y, N, T, Q, B)
	else:
		Lambda[0,i] = test_statistic_TR(F, Y, N, T, Q)
		Lambda[1,i] = test_statistic_CR_beta(beta, F, Y, N, T, Q)
		Lambda[2,i] = test_statistic_CR_intercept(F, Y, N, T, Q)

# Time-Series Regression Plot
plt.figure('Figure 1')
n, bins, patches = plt.hist(Lambda[0,:], bins = 50, normed = 1, facecolor = 'yellow', alpha = 0.5)
f_normal = mlab.normpdf(bins, 1, np.sqrt(2.0 / (1 - y) / N))
f_chi2_1 = N * chi2.pdf(bins * N, N)
f_chi2_0 = N * T * 1.0 / (T - N - Q) * chi2.pdf(bins * N * T * 1.0 / (T - N - Q), N)
line_chi2_1, = plt.plot(bins, f_chi2_1, 'r--', linewidth = 3, label = r'$\Lambda_{TR,1}$')
line_chi2_0, = plt.plot(bins, f_chi2_0, 'g-.', linewidth = 3, label = r'$\Lambda_{TR,0}$')
line_normal, = plt.plot(bins, f_normal, 'b-', linewidth = 3, label = r'$\Lambda_{TR}$')
plt.legend(frameon = False, handles = [line_chi2_0, line_chi2_1, line_normal])
plt.xlabel(r'$\Lambda_{TR}$')
plt.ylabel('Probability Density')
plt.title('N='+str(N)+',T='+str(T)+',k='+str(Q))
plt.savefig('./output/distributions/n%d_t%d_q%d_e%s_TR.jpeg' % (N, T, Q, args.E))

# Cross-Sectional Regression Plot (beta)
plt.figure('Figure 2')
n, bins, patches = plt.hist(Lambda[1,:], bins = 50, normed = 1, facecolor = 'yellow', alpha = 0.5)
f_normal = mlab.normpdf(bins, 1, np.sqrt(2 * (1 - y) / (N - Q)))
f_chi2_1 = (N - Q) * chi2.pdf(bins * (N - Q), N - Q)
line_normal, = plt.plot(bins, f_normal, 'b-', linewidth = 3, label = r'$\Lambda_{CR}^{\beta}$')
line_chi2_1, = plt.plot(bins, f_chi2_1, 'r--', linewidth = 3, label = r'$\Lambda_{CR,1}^{\beta}$')
plt.legend(frameon = False, handles = [line_chi2_1, line_normal])
plt.xlabel(r'$\Lambda_{CR}^{\beta}$')
plt.ylabel('Probability Density')
plt.title('N='+str(N)+',T='+str(T)+',k='+str(Q))
plt.savefig('./output/distributions/n%d_t%d_q%d_e%s_CR_beta.jpeg' % (N, T, Q, args.E))

# Cross-Sectional Regression Plot
plt.figure('Figure 3')
n, bins, patches = plt.hist(Lambda[2,:], bins = 50, normed = 1, facecolor = 'yellow', alpha = 0.5)
f_normal = mlab.normpdf(bins, 1, np.sqrt(2 * (1 - y) / (N - Q)))
f_chi2_1 = (N - Q) * T * 1.0 / (T - Q) * chi2.pdf(bins * (N - Q) * T * 1.0 / (T - Q), N - Q)
line_normal, = plt.plot(bins, f_normal, 'b-', linewidth = 3, label = r'$\Lambda_{CR}$')
line_chi2_1, = plt.plot(bins, f_chi2_1, 'r--', linewidth = 3, label = r'$\Lambda_{CR,1}$')
plt.legend(frameon = False, handles = [line_chi2_1, line_normal])
plt.xlabel(r'$\Lambda_{CR}$')
plt.ylabel('Probability Density')
plt.title('N='+str(N)+',T='+str(T)+',k='+str(Q))
plt.savefig('./output/distributions/n%d_t%d_q%d_e%s_CR.jpeg' % (N, T, Q, args.E))