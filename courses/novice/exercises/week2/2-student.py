#!/usr/bin/env python
answer = []
data = [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13, [100,200, 300, 400, ['FOO'] ], 14,15] ]

#check 4 levels
#if len doesn't reaise typeerror, check if it's a string, if it is, append and continue with next element, if not, go down one more level and check len of each element
#if len raises the typeerror, append the current element and continue with the next element

data.insert(2, 'A')

for i in range(len(data)):
    try:
	len(data[i])
	if type(data[i]) is str:
	    answer.append(data[i])
	    continue
    except TypeError as error:
	answer.append(data[i])
    else:
	for j in range(len(data[i])):
	    try:
		len(data[i][j])
		if type(data[i][j]) is str:
		    answer.append(data[i][j])
		    continue
   	    except TypeError as error:
		answer.append(data[i][j])
	    else:
		for k in range(len(data[i][j])):
		    try:
			len(data[i][j][k])
			if type(data[i][j][k]) is str:
			    answer.append(data[i][j][k])
			    continue
   		    except TypeError as error:
			answer.append(data[i][j][k])
		    else:
			for l in range(len(data[i][j][k])):
			    try:
				len(data[i][j][k][l])
				if type(data[i][j][k][l]) is str:
				    answer.append(data[i][j][k][l])
				    continue
   			    except TypeError as error:
				answer.append(data[i][j][k][l])

assert answer == [1,2,3,4,5,6,7,8, 9,10, 'A', 11,12,13, 100, 200, 300, 400, 'FOO', 14,15], answer
