import numpy as np 

lev_0 = np.array(
	[[None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None],
	 [None, None, None, None, None, None, None, None, None]])

lev_1 = np.array(
	[[None, None, None, None, None, None, 5, None, None],
	 [3, None, 2, None, 7, None, 9, 1, None],
	 [6, None, None, 9, None, None, None, None, None],
	 [None, None, None, None, None, None, None, 2, 6],
	 [None, 2, None, 3, None, None, 1, 5, 9],
	 [7, 9, None, 6, None, 5, None, 8, None],
	 [1, None, 9, 7, None, None, None, None, None],
	 [4, 5, None, None, None, None, 2, 3, None],
	 [None, 3, 8, 4, 5, None, 6, None, None]])

lev_2 = np.array(
	[[None, 1, 7, None, None, None, None, None, 4],
	 [None, 9, 3, None, 5, None, None, 2, None],
	 [2, None, 5, None, 8, None, 7, 1, 3],
	 [None, None, None, None, None, None, None, 4, 7],
	 [None, None, 1, 6, None, 2, 9, None, None],
	 [6, 8, None, None, None, None, None, None, None],
	 [1, 5, 8, None, 6, None, 2, None, 9],
	 [None, 4, None, None, 7, None, 3, 5, None],
	 [7, None, None, None, None, None, 4, 6, None]])

lev_3 = np.array(
	[[None, 8, None, None, 2, None, None, None, 6],
	 [None, 9, 2, None, 5, None, 7, None, None],
	 [None, None, None, 6, None, 1, None, None, 3],
	 [None, 7, None, None, None, None, None, None, None],
	 [5, None, 3, None, None, None, 9, None, 4],
	 [None, None, None, None, None, None, None, 8, None],
	 [4, None, None, 7, None, 3, None, None, None],
	 [None, None, 7, None, 4, None, 8, 3, None],
	 [1, None, None, None, 9, None, None, 5, None]])

lev_4 = np.array(
	[[6, None, 7, None, None, 2, None, None, None],
	 [4, None, None, 9, None, None, None, None, 8],
	 [None, None, None, None, 7, 4, 6, 1, None],
	 [None, 6, None, None, None, None, 2, None, None],
	 [None, 9, None, None, None, 8, None, 7, None],
	 [None, None, 4, 7, None, None, None, 9, None],
	 [None, 8, 5, 2, 4, None, None, None, None],
	 [9, None, None, None, None, 6, None, None, 1],
	 [None, None, None, None, 8, None, 9, None, 5]])

lev_5 = np.array(
	[[1, None, None, None, None, 4, None, None, 6],
	 [None, 4, None, None, None, 2, None, None, None],
	 [None, None, 5, None, 8, 9, None, None, None],
	 [None, None, None, None, None, None, None, 2, None],
	 [None, 9, 6, None, None, None, 1, 4, None],
	 [None, None, 3, None, None, None, None, None, None],
	 [None, None, None, 7, 1, None, 6, None, None],
	 [2, None, None, 3, None, None, None, 7, None],
	 [5, None, None, 4, None, None, None, None, 8]])