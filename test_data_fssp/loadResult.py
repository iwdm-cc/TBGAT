import numpy as np
loaded_arr = np.load('ortools_result_FSSP-tai20x5[0,10]_result.npy')
print(loaded_arr)

loaded_arr = np.load('ortools_result_FSSP-tai20x5[0,10]_time.npy')
print(len(loaded_arr))

loaded_arr = np.load('tai20x5.npy')
print(loaded_arr)