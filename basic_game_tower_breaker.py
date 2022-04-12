def towerBreakers(n, m):
    # Write your code here
    print(n)
    print(m)
    towers = [m] * n
    print(towers)
    return 0


if __name__ == '__main__':
    t = 2
    first_multiple_input = [[2, 3], [6, 7]]
    for t_itr in range(t):
        n = first_multiple_input[0][t_itr]

        m = first_multiple_input[1][t_itr]

        result = towerBreakers(n, m)
