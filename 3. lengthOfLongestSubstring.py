def lengthOfLongestSubstring(s):
	stack = []
	i = 0
	word_lst = [""]
	while i < len(s):
		if s[i] not in stack:
			stack.append(s[i])
		else:
			word = ""
			while len(stack) > 0:
				word += stack.pop()
			if len(word) > len(word_lst[0]):
				word_lst[0] = word

			stack.append(s[i])
		i +=1

	return len(word_lst[0])

if __name__ == '__main__':
	string = "abcabcbb"
	print(lengthOfLongestSubstring(string))
	print(lengthOfLongestSubstring("bbbbb"))
	print(lengthOfLongestSubstring("pwwkew"))
