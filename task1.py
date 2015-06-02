def findPalindromes(word):
	for n in range(0, len(word)):
		if isPalindrome(word[n:] + word[:n]):
			print(word[n:] + word[:n])


def isPalindrome(word):
	return word == word[::-1]


def main():
	word = input("Enter word: ")
	findPalindromes(word)


if __name__ == "__main__":
	main()