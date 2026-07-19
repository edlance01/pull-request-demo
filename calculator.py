def add(a, b):
    return a + b


def divide(a, b):
    # Intentional bug for the demo: we forgot to handle division by zero!
    return a / b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
