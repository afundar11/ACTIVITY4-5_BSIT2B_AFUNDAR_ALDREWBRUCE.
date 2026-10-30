
def balanced_parentheses(expression):
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in expression:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if not stack:
                return False

            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0


expression = input("Enter an expression: ")

if balanced_parentheses(expression):
    print("The parentheses are balanced.")
else:
    print("The parentheses are NOT balanced.")
