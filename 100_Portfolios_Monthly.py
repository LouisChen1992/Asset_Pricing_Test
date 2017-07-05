from utils_fama_french import *

with open('output/fama_french/100_Portfolios_Monthly.txt', 'w') as file:
	# 100 Portfolios, Monthly Data, 1978/07 - 1999/06
	# Longest Period With No Missing Values
	r = load_data('data/100_Portfolios_10x10.CSV', 645, 896)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 629, 880)
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1978/07', '1999/06'), N, T, file)

	# 100 Portfolios, Monthly Data, 1973/01 - 2016/10
	# The Period Has Only 101 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {97: 12, 98: 12, 99: 65, 69: 12} 
	r = load_data('data/100_Portfolios_10x10.CSV', 579, 1104)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 563, 1088)
	replacement = dict()
	for i in xrange(1104 - 579 + 1):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1973/01', '2016/10'), N, T, file)

	###################################################################################

	# 100 Portfolios, Monthly Data, 10 Year Horizons
	# The Period Has Only 48 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {97: 12, 98: 12, 99: 24}
	r = load_data('data/100_Portfolios_10x10.CSV', 579, 698)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 563, 682)
	replacement = dict()
	for i in xrange(120):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1973/01', '1982/12'), N, T, file)

	# The Period Has No Missing Values. 
	r = load_data('data/100_Portfolios_10x10.CSV', 699, 818)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 683, 802)
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1983/01', '1992/12'), N, T, file)

	# The Period Has Only 29 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {99: 17, 69: 12}
	r = load_data('data/100_Portfolios_10x10.CSV', 819, 938)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 803, 922)
	replacement = dict()
	for i in xrange(120):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1993/01', '2002/12'), N, T, file)

	# The Period Has Only 24 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {99: 24}
	r = load_data('data/100_Portfolios_10x10.CSV', 939, 1058)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 923, 1042)
	replacement = dict()
	for i in xrange(120):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '2003/01', '2012/12'), N, T, file)

	###################################################################################

	# 100 Portfolios, Monthly Data, 20 Year Horizons
	# The Period Has Only 48 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {97: 12, 98: 12, 99: 24}
	r = load_data('data/100_Portfolios_10x10.CSV', 579, 818)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 563, 802)
	replacement = dict()
	for i in xrange(240):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1973/01', '1992/12'), N, T, file)

	# The Period Has Only 53 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {99: 41, 69: 12}
	r = load_data('data/100_Portfolios_10x10.CSV', 819, 1058)
	f = load_data('data/F-F_Research_Data_Factors.CSV', 803, 1042)
	replacement = dict()
	for i in xrange(240):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[:-1]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1993/01', '2012/12'), N, T, file)