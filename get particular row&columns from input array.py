# Return array of odd rows and even columns from below numpy array

s = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print('Input array', s)

print('Odd rows and even columns from input numpy array is', s[::2, 1::2])