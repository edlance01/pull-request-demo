def add(a, b):
    return a + b


def divide(a, b):
   if b == 0:
        raise ValueError("Cannot divide by zero.")
   return a / b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")  # This will raise an exception
