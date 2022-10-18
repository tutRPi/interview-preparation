import math


def setup(adj_matrix, memo, starting_index, N):
    for i in range(N):
        if i == starting_index:
            continue
        # store the optimal value from node S to node i
        # S = 0, i = 3 => memo[3][0b1001] = matrix[0][3] (distance matrix)
        memo[i][1 << starting_index | 1 << i] = adj_matrix[starting_index][i]


def solve(adj_matrix, memo, starting_index, N):
    for r in range(3, N):
        # function creates all bit sets of size N with r bits set to 1:
        # For example combinations(3, 4) = {0b0111, 0b1011, 0b1101, 0b1110
        for subset in combinations(r, N):
            if not_in(starting_index, subset):
                continue
            for next in range(N):
                if next == starting_index or not_in(next, subset):
                    continue
                # the subset node without the next node
                state = subset ^ (1 << next)
                min_dist = math.inf
                for e in range(N):
                    if e == starting_index or e == next or not_in(e, subset):
                        continue
                    new_distance = memo[e][state] + adj_matrix[e][next]
                    if new_distance < min_dist:
                        min_dist = new_distance
                memo[next][subset] = min_dist


def not_in(i, subset):
    return ((1 << i) & subset) == 0


def combinations(r, n) -> list:
    subsets = []
    rec_combinations(0, 0, r, n, subsets)
    return subsets


def rec_combinations(bitset, at, r, n, subsets):
    if r == 0:
        subsets.append(bitset)
    else:
        for i in range(at, n):
            # Flip i-th bit
            bitset = bitset | (1 << i)
            rec_combinations(bitset, i + 1, r - 1, n, subsets)

            bitset = bitset & ~(1 << i)


def find_min_cost(adj_matrix, memo, starting_index, N):
    END_STATE = (1 << N) - 1
    min_tour_cost = math.inf
    for e in range(N):
        if e == starting_index:
            continue
        tour_cost = memo[e][END_STATE] + adj_matrix[e][starting_index]
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
    return min_tour_cost


def find_optimal_tour(adj_matrix, memo, starting_index, N):
    last_index = starting_index
    state = (1 << N) - 1
    tour = [None] * (N + 1)
    for i in reversed(range(1, N)):
        index = -1
        for j in range(N):
            if j == starting_index or not_in(j, state):
                continue
            if index == -1:
                index = j
            prev_dist = memo[index][state] + adj_matrix[index][last_index]
            new_dist = memo[j][state] + adj_matrix[j][last_index]
            if new_dist < prev_dist:
                index = j
        tour[i] = index
        state = state ^ (1<<index)
        last_index = index
    tour[0] = tour[N] = starting_index
    return tour


def tsp(adj_matrix, starting_index):
    N = len(adj_matrix)

    memo = [[None] * (2 ** N)] * N
    setup(adj_matrix, memo, starting_index, N)
    solve(adj_matrix, memo, starting_index, N)
    min_index = find_min_cost(adj_matrix, memo, starting_index, N)
    tour = find_optimal_tour(adj_matrix, memo, starting_index, N)

    return min_index, tour

