
from ArrayStack import ArrayStack
from LinkedStack import LinkedStack
from CircularArrayQueue import CircularArrayQueue
from LinkedQueue import LinkedQueue


def operate(data_structure, is_stack):
    while True:
        print("\n1. Add value")
        print("2. Remove value")
        print("3. View top/front")
        print("4. Display")
        print("5. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                value = input("Enter value: ")

                if is_stack:
                    data_structure.push(value)
                else:
                    data_structure.enqueue(value)

                print("Value added successfully.")

            elif choice == "2":
                if is_stack:
                    print("Removed:", data_structure.pop())
                else:
                    print("Removed:", data_structure.dequeue())

            elif choice == "3":
                if is_stack:
                    print("Top value:", data_structure.peek())
                else:
                    print("Front value:",
                          data_structure.peek_front())

            elif choice == "4":
                data_structure.display()

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except (IndexError, OverflowError) as error:
            print("Error:", error)


def main():
    while True:
        print("\n=== STACKS AND QUEUES ===")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Exit")

        choice = input("Choose implementation: ")

        if choice == "1":
            operate(ArrayStack(3), True)

        elif choice == "2":
            operate(LinkedStack(), True)

        elif choice == "3":
            operate(CircularArrayQueue(3), False)

        elif choice == "4":
            operate(LinkedQueue(), False)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
