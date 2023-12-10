class Solution:
	def isSame(self, s):
		s_list = s.split(s.isnumeric())
		print(s_list)
		numeric_indicies = []
		for i in range(len(s_list)):
			if s[i].isnumeric():
				numeric_indicies.append(i)
			else:
				continue
		print(numeric_indicies)
		length_of_letters = s[:int(numeric_indicies[0])]
		if length_of_letters == int(s[-1]):
			return 1
		else:
		    return 0
    

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)