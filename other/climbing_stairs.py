def climbing_stairs(n: int):
    if n <= 2:
        return n
    return climbing_stairs(n - 1) + climbing_stairs(n - 2)


if __name__ == "__main__":
    assert climbing_stairs(5) == 8
