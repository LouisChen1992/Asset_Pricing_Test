from utils_fama_french import *

with open('output/fama_french/100_Portfolios_Monthly_Size_Profitability.txt','w') as file:
	# 100 Portfolios, Monthly Data, 1963/07 - 2016/12
	# The Period Has Only 24 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {80: 12, 90: 12} 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 18, 659)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 5, 646)
	replacement = dict()
	for i in xrange(659 - 18 + 1):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1963/07', '2016/12'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	###################################################################################

	# 100 Portfolios, Monthly Data, 10 Year Horizons
	# The Period Has Only 12 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {80: 12} 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 18, 137)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 5, 124)
	replacement = dict()
	for i in xrange(137 - 18 + 1):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1963/07', '1973/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	# The Period Has No Missing Values. 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 138, 257)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 125, 244)
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1973/08', '1983/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	# The Period Has No Missing Values. 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 258, 377)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 245, 364)
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1983/07', '1993/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	# The Period Has No Missing Values. 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 378, 497)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 365, 484)
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1993/07', '2003/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	# The Period Has Only 12 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {90: 12}
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 498, 617)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 485, 604)
	replacement = dict()
	for i in xrange(617 - 498 + 1):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '2003/07', '2013/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	###################################################################################

	# 100 Portfolios, Monthly Data, 20 Year Horizons
	# The Period Has Only 12 Missing Values, Which Are Replaced With 0.
	# Replaced With 0: {80: 12} 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 18, 257)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 5, 244)
	replacement = dict()
	for i in xrange(257 - 18 + 1):
		for j in xrange(100):
			if r.T[i,j] == -99.99:
				r.T[i,j] = 0
				replacement[j] = replacement.get(j,0) + 1
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1963/07', '1983/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])

	# The Period Has No Missing Values. 
	r = load_data('data/100_Portfolios_ME_OP_10x10.CSV', 258, 497)
	f = load_data('data/F-F_Research_Data_5_Factors_2x3.CSV', 245, 484)
	RF = f[-1]
	F = f[[0,1,3]]
	Y = r - RF
	q, T = F.shape
	N = Y.shape[0]
	display(result(F, Y, T, N, q), ('Monthly', '1983/07', '2003/06'), N, T, f = file, Factors = ['Mkt-RF', 'SMB', 'RMW'])