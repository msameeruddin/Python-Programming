def number_digits_to_word(number):
		
		number_directry = {
			1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
			11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "forteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 
			18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 
			80 : "eighty", 90 : "ninety", 1000 : "one thousand"
		}
		
		output_string = list()
		
		if (number <= 0 or number > 1000):
			return -1
		else:
			digits = list()
			given_num = number
			
			if (given_num > 0 and given_num <= 20):
				digits.append(given_num)
			else:
				zero_index = list()
				
				i = 1
				while (given_num != 0):
					num = given_num % 10
					actual = num * i
					digits.append(actual)
					given_num //= 10
					i *= 10
				
				if (10 in digits):
					tenth = digits.pop(digits.index(10))
					digits[0] = digits[0] + tenth
				
				for i in digits:
					if (i == 0):
						zero_index.append(i)
				
				for i in range(0, len(zero_index), 1):
					digits.remove(digits[zero_index[i]])
					
			digits.reverse()
			
			for i in digits:
				if i == 1000:
					output_string.append(number_directry[i])
				elif i % 100 == 0 and len(digits) > 1:
					digit_extract_100 = i // 100
					output_string.append(number_directry[digit_extract_100] + " hundred and")
				elif i % 100 == 0 and len(digits) == 1:
					digit_extract_100 = i // 100
					output_string.append(number_directry[digit_extract_100] + " hundred")
				else:
					output_string.append(number_directry[i])
			
			output_string = " ".join(output_string)
			return output_string

print(number_digits_to_word(number=999))