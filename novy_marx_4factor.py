from utils_novy_marx import *

r = load_return_data()
f = load_factor_data()
RF = f[-1]
F = f[:-1]
Y = r - RF

with open('output/novy_marx/150asset_4factor.txt', 'a') as file:
	Y_test = Y[:150]
	F_test = F[[2,9,11,15]]
	N_test = Y_test.shape[0]
	q_test = F_test.shape[0]

	T_test = 600 # 600 months
	display(result(F_test[:,6:606], Y_test[:,6:606], T_test, N_test, q_test), ('Monthly', '1964/01', '2013/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,6:606], Y_test[:,6:606], T_test, N_test, q_test), ('Monthly', '1964/01', '2013/12'), N_test, T_test, q_test, file)

	T_test = 300 # 300 months
	display(result(F_test[:,6:306], Y_test[:,6:306], T_test, N_test, q_test), ('Monthly', '1964/01', '1988/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,6:306], Y_test[:,6:306], T_test, N_test, q_test), ('Monthly', '1964/01', '1988/12'), N_test, T_test, q_test, file)
	display(result(F_test[:,306:606], Y_test[:,306:606], T_test, N_test, q_test), ('Monthly', '1989/01', '2013/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,306:606], Y_test[:,306:606], T_test, N_test, q_test), ('Monthly', '1989/01', '2013/12'), N_test, T_test, q_test, file)

	T_test = 240 # 20 years
	display(result(F_test[:,6:246], Y_test[:,6:246], T_test, N_test, q_test), ('Monthly', '1964/01', '1983/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,6:246], Y_test[:,6:246], T_test, N_test, q_test), ('Monthly', '1964/01', '1983/12'), N_test, T_test, q_test, file)
	display(result(F_test[:,246:486], Y_test[:,246:486], T_test, N_test, q_test), ('Monthly', '1984/01', '2003/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,246:486], Y_test[:,246:486], T_test, N_test, q_test), ('Monthly', '1984/01', '2003/12'), N_test, T_test, q_test, file)

	T_test = 200 # 200 months
	display(result(F_test[:,6:206], Y_test[:,6:206], T_test, N_test, q_test), ('Monthly', '1966/01', '1980/08'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,6:206], Y_test[:,6:206], T_test, N_test, q_test), ('Monthly', '1966/01', '1980/08'), N_test, T_test, q_test, file)
	display(result(F_test[:,206:406], Y_test[:,206:406], T_test, N_test, q_test), ('Monthly', '1980/09', '1997/04'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,206:406], Y_test[:,206:406], T_test, N_test, q_test), ('Monthly', '1980/09', '1997/04'), N_test, T_test, q_test, file)
	display(result(F_test[:,406:606], Y_test[:,406:606], T_test, N_test, q_test), ('Monthly', '1997/05', '2013/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,406:606], Y_test[:,406:606], T_test, N_test, q_test), ('Monthly', '1997/05', '2013/12'), N_test, T_test, q_test, file)

	T_test = 180 # 15 years
	display(result(F_test[:,6:186], Y_test[:,6:186], T_test, N_test, q_test), ('Monthly', '1964/01', '1978/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,6:186], Y_test[:,6:186], T_test, N_test, q_test), ('Monthly', '1964/01', '1978/12'), N_test, T_test, q_test, file)
	display(result(F_test[:,186:366], Y_test[:,186:366], T_test, N_test, q_test), ('Monthly', '1979/01', '1993/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,186:366], Y_test[:,186:366], T_test, N_test, q_test), ('Monthly', '1979/01', '1993/12'), N_test, T_test, q_test, file)
	display(result(F_test[:,366:546], Y_test[:,366:546], T_test, N_test, q_test), ('Monthly', '1994/01', '2008/12'), N_test, T_test, q_test, file)
	display_cross(result_cross(F_test[:,366:546], Y_test[:,366:546], T_test, N_test, q_test), ('Monthly', '1994/01', '2008/12'), N_test, T_test, q_test, file)