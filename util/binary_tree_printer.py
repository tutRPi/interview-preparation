def print_binary_tree(root_node):
    def __get_depth(node):
        if node is None:
            return 0
        return max(__get_depth(node.left), __get_depth(node.right)) + 1

    def __add(node, height_offset: int, width_offset: int):
        # add to list
        lines[height_offset][width_offset] = node.data
        if node.left is not None:
            __add(node.left, height_offset + 1, 2 * width_offset)
        if node.right is not None:
            __add(node.right, height_offset + 1, 2 * width_offset + 1)

    if root_node is None:
        return
    depth = __get_depth(root_node)
    lines = [[None for j in range(pow(2, i))] for i in range(depth)]
    __add(root_node, 0, 0)

    for i, line in enumerate(lines):
        offset = (2 ** (depth - i)) - 1
        left_offset = int(offset / 2)

        # print lines
        if i != 0:
            print(" " * left_offset, end="")
            for j, x in enumerate(lines[i]):
                if x is not None:
                    if j % 2 == 0:
                        print("/", end='')
                    else:
                        print("\\", end='')
                else:
                    print(" ", end='')
                print(" " * offset, end='')
            print()

        print(" " * left_offset, end="")
        for j, x in enumerate(line):
            if x is not None:
                print(x, end='')
                print(" " * max(0, offset + 1 - len(str(x))), end='')
            else:
                print(" " * (offset + 1), end='')
        print() # end of line
