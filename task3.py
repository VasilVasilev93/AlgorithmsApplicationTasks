class Stack:
	def __init__(self):
		self.size = 0
		self.content = []

	def Top(self):
		if self.size == 0:
			return
		return self.content[self.size-1]

	def push(self, x):
		self.size += 1
		self.content.append(x)

	def pop(self):
		if self.size > 0:
			del self.content[-1]
			self.size -= 1
		return

	def isEmpty(self):
		if self.size == 0:
			return True
		return False

	def reset(self):
		self.size = 0
		self.content = []


class Bracket:
	def __init__(self, symbol, priority):
		self.symbol = symbol
		self.priority = priority


openRound = Bracket('(', 1)
closeRound = Bracket(')', 1)

openSquare = Bracket('[', 2)
closeSquare = Bracket(']', 2)

openCurly = Bracket("{", 3)
closeCurly = Bracket("}", 3)

openBrackets = []
closeBrackets = []

openBrackets.extend((openRound, openSquare, openCurly))
closeBrackets.extend((closeRound, closeSquare, closeCurly))


brackets = Stack()


def arePair(opening, closing):
	if opening == openRound.symbol and closing == closeRound.symbol:
		return True
	if opening == openSquare.symbol and closing == closeSquare.symbol:
		return True
	if opening == openCurly.symbol and closing == closeCurly.symbol:
		return True
	return False


def openBracketFound(symbol):
	for n in openBrackets:
		if symbol == n.symbol:
			return True
	return False


def closeBracketFound(symbol):
	for n in closeBrackets:
		if symbol == n.symbol:
			return True
	return False


def findTypeOfBracket(symbol):
	for n in openBrackets:
		if symbol == n.symbol:
			return n


def isBracket(symbol):
	if symbol in "{[()]}":
			return True
	return False


def validateOnlyRound(expression):
    if openRound.symbol not in expression and closeRound.symbol not in expression:
        return True
    start = expression.find(openRound.symbol)
    end = expression[::-1].find(closeRound.symbol)
    end = len(expression) - end
    if (start == -1 and end != -1) or (start != -1 and end == -1):
        return False
    if end < start:
        return False
    check = expression[start:end]
    error = [openSquare.symbol, closeSquare.symbol, openCurly.symbol, closeCurly.symbol]
    for each in error:
        if each in check:
            return False
    return True


def checkNested(expression):
    opening = expression[0]
    for i in range(1, len(expression) - 1):
        if expression[i] == opening:
            return False
    return True


def validate(expression):
	if not isBracket(expression[0]) or not isBracket(expression[-1]) or not validateOnlyRound(expression) or not checkNested(expression):
		return False

	for i in range(0, len(expression)):
		if isBracket(expression[i]):
			if openBracketFound(expression[i]):
				if brackets.isEmpty():
					brackets.push(expression[i])
				else:
					otherBracket = findTypeOfBracket(brackets.Top())
					currentBracket = findTypeOfBracket(expression[i])

					if currentBracket.priority >= otherBracket.priority or otherBracket.priority - currentBracket.priority == 2:
						return False
					brackets.push(expression[i])

			else:
				if brackets.isEmpty() or not arePair(brackets.Top(), expression[i]):
					return False
				else:
					brackets.pop()
	brackets.reset()
	return True


def trimExpression(expression):
    expression = expression.replace('+)', '+0)')
    expression = expression.replace('()', '(0)')
    return expression


def translateExpression(expression):
    for n in "()[]{}":
        if n in expression:
            if openCurly.symbol in expression or closeCurly.symbol in expression:
                if n == openCurly.symbol:
                    expression = expression.replace(openCurly.symbol, '(')
                if n == closeCurly.symbol:
                    expression = expression.replace(closeCurly.symbol, ')+')

                if (n == '(' or n == '['):
                    expression = expression.replace(n, '+2*(')
                if n == ")" or n == "]":
                    expression = expression.replace(n, ')+')

            elif openCurly.symbol not in expression:
                if n == '(':
                    expression = expression.replace(n, '+2*(')
                if n == '[':
                    expression = expression.replace(n, '(')
                if n == ']' or n == ')':
                    expression = expression.replace(n, ')+')
            elif '(' not in expression:
                expression = expression.replace(n, '(')
                expression = expression.replace(n, ')')
                return expression
            else:
                return expression

    expression = trimExpression(expression)
    return expression[:-1].replace('++', '+')


def calculate(expression):
	if validate(expression):
		return eval(translateExpression(expression))
	return("Expression invalid")


def main():
	print(calculate("{123[123(123)123(123)]23[123]2}"))
	print(calculate("[123(145)38(37)812]"))
	print(calculate("[125()125()125()125]"))
	print(calculate("{125[2][(1)][3]125}"))
	print(calculate("{125()125}"))
	print(calculate("{125[12]{125}[12]125}"))
	print(calculate("{125[12(123]125}"))

if __name__ == '__main__':
    main()