def getOriginalEncrypt(string):
	return string[len(string)//2:] + string[:len(string)//2]


def deCrypt(string):
	originalEncrypt = getOriginalEncrypt(string)

	elements = originalEncrypt.split("~")
	lengthOfAlphabet = int(elements[0])
	lengthOfKey = int(elements[2])

	alphabet = elements[1][:lengthOfAlphabet]
	key = elements[1][-lengthOfKey:]
	encryptedWord = elements[1][lengthOfAlphabet:len(elements[1])-lengthOfKey]

	keyedWord = ""
	for n in range(0,len(encryptedWord)):
		keyedWord += key[n%lengthOfKey]

	originalWord = ""

	for n in range(0, len(encryptedWord)):
		originalWord += alphabet[(alphabet.index(encryptedWord[n]) - \
		alphabet.index(keyedWord[n])) % lengthOfAlphabet]

	return originalWord


def main():
	string = input("Enter encrypted string: ")
	deCrypt(string)



if __name__ == '__main__':
	main():
