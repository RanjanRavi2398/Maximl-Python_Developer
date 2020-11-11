
no_of_chars= 256
def max_distinct_char(str, n): 
	count = [0] * no_of_chars
	for i in range(n): 
		count[ord(str[i])] += 1
	
	max_distinct = 0
	for i in range(no_of_chars): 
		if (count[i] != 0): 
			max_distinct += 1	
	
	return max_distinct 

def smallesteSubstr_maxDistictChar(str): 

	n = len(str)	 
	max_distinct = max_distinct_char(str, n) 
	minl = n	
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_lenght = len(subs) 
			sub_distinct_char = max_distinct_char(subs, 
												subs_lenght) 
			
			
			if (subs_lenght < minl and
				max_distinct == sub_distinct_char): 
				minl = subs_lenght 

	return minl 


if __name__ == "__main__": 
	
	str = str(input())
	l = smallesteSubstr_maxDistictChar(str); 
	print(l) 

