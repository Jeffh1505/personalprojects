class Solution:
    def isSame(self, s):
        if not s.isnumeric():
            return 0
        
        length = len(s) - 1 if s[-1] != '0' else len(s) - 2
        print(length)
        last_digit = int(s[-1])
        print(last_digit)
        return 1 if length == last_digit else 0
    

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)