from calculator.calculations import Add, Subtract
from calculator.history import History


class Calculator:
    def __init__(self):
        self.history = History()

    def run(self) -> None:
        while True:
            try:
                cmd = input("> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            if cmd == "exit":
                print("Goodbye!")
                break
            elif cmd == "help":
                self.show_help()
            elif cmd in ("add", "subtract"):
                self.handle_operation(cmd)
            elif cmd == "history":
                self.show_history()
            elif cmd == "remove":
                self.handle_remove()
            elif cmd == "":
                continue
            else:
                print(f"Unknown command: {cmd}")

    def show_help(self) -> None:
        print("Available commands:")
        print("  add       - Add two numbers")
        print("  subtract  - Subtract the second number from the first")
        print("  history   - Show calculation history")
        print("  remove    - Remove an item from history by number")
        print("  help      - Show this help message")
        print("  exit      - Exit the calculator")

    def handle_operation(self, op_name: str) -> None:
        try:
            a_val = float(input("First number: "))
            b_val = float(input("Second number: "))
        except ValueError:
            print("Invalid input: Please enter numeric values.")
            return

        if op_name == "add":
            calc = Add(a_val, b_val)
        else:
            calc = Subtract(a_val, b_val)

        result = calc.execute()
        # Format integer floats cleanly (e.g. 15.0 -> 15)
        if result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)

        print(f"Result: {result_str}")
        self.history.add(calc)

    def show_history(self) -> None:
        records = self.history.all()
        if not records:
            print("History is empty.")
            return

        print("Calculation History\n")
        for i, record in enumerate(records, start=1):
            print(f"{i}. {record}")

    def handle_remove(self) -> None:
        try:
            index = int(input("Enter history number to remove: "))
            self.history.remove(index)
            print(f"Removed item {index}.")
        except (ValueError, IndexError):
            print("Invalid history entry.")