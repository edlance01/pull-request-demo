from calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5
    # The pull request will later add a test for dividing by zero!
