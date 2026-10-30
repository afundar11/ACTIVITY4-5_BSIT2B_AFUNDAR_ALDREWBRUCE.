
import ArrayStack


stack = ArrayStack.ArrayStack(2)

print("--- UNDERFLOW TEST ---")

try:
    stack.pop()
except IndexError as error:
    print("Error:", error)

print("\n--- OVERFLOW TEST ---")

try:
    stack.push("A")
    stack.push("B")
    stack.push("C")
except OverflowError as error:
    print("Error:", error)
