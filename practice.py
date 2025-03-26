def fibonacci(n: int) -> int:
    "fibonacci number finder"
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(13))

PI: float = 3.14
print(PI)


grocery_list: list[str] = ["bananas", "milk", "bread"]
grocery_list[0]

list: list[int] = [1, 2, 3, 4]
list[3]


def reverse(xs: list[str]) -> list[str]:
    idx: int = len(xs) - 1
    result: list[str] = []
    while idx >= 0:
        result.append(xs[idx])
        idx -= 1
    return result


self: str = ["me", "you", "I"]
reverse(xs=self)
