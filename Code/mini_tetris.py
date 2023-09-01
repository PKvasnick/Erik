
# Dlzky a kody dielikov

parts = [
    ("\U00002589", 2),              # ▉
    ("\U00002599\U0000259D",2),     # ▙▝
    ("\U0000259B\U00002597",2),     # ▛▗
    ("\U0000258B", 1),              # ▋
    ("\U0000259A", 1)               # ▚
]


def print_column(column: list[str]) -> None:
    print(" ".join(column))


def generate(n:int) -> None:
    stack = []
    stack.append(([], 0))
    n_solutions = 0
    while stack:
        column, length = stack.pop()
        for part in parts:
            column.append(part[0])
            new_length = length + part[1]
            if new_length < n:
                stack.append((column[:], new_length))
            elif new_length == n:
                print_column(column)
                n_solutions += 1
            column.pop()

    print(f"{n_solutions} rieseni.")


def main():
    print(parts)
    generate(3)


if __name__ == "__main__":
    main()
