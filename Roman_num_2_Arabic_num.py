
roman_numerals = {
		"M": 1000,
		"D": 500,
		"C": 100,
		"L": 50,
		"X": 10,
		"V": 5,
		"I": 1,
	}

def convert_to_num_array(str):
	result = []
	temp = str[0]
	for x in range(1,len(str)):
		if str[x] == str[x-1]:
			temp += str[x]
		else:
			result.append(temp)
			temp = ''
			temp = str[x]
		if x == len(str)-1:
			result.append(temp)
			
	print(result)
	
	def convert_roman_numerals_to_num(x):
		return roman_numerals[x[0]] * len(x)
	
	result = list(map(convert_roman_numerals_to_num, result))

	print(result)
	return result
	
def R2D(str):

	num_arry = convert_to_num_array(str)
	num_arry.reverse()
	
	result = num_arry[0]
	
	for k in range(1,len(num_arry)):
		if(num_arry[k-1] < num_arry[k]):
			result += num_arry[k]
		elif(num_arry[k-1] >  num_arry[k]):
			result -= num_arry[k]

	print(str, '->', result)
		
		
R2D('MMMDCCCXCIV')