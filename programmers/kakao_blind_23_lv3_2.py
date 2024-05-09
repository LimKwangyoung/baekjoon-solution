import collections


def solution(commands):
    result = []

    table = [['EMPTY'] * 51 for _ in range(51)]
    values = collections.defaultdict(str)

    for command in commands:
        cmd, *info = command.split()

        if cmd == 'UPDATE':
            if len(info) == 2:
                value1, value2 = info
                values[value1] = value2
            elif len(info) == 3:
                r, c, value = info
                r = int(r)
                c = int(c)
                # already merged
                if len(table[r][c]) == 2:
                    (r1, c1, r2, c2), _ = table[r][c]
                    for i in range(r1, r2 + 1):
                        for j in range(c1, c2 + 1):
                            table[i][j][-1] = value
                # not merged
                else:
                    table[r][c] = value

        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, info)
            if (r1, c1) != (r2, c2):
                # update the range
                min_row, max_row = min(r1, r2), max(r1, r2)
                min_col, max_col = min(c1, c2), max(c1, c2)
                for i in range(min_row, max_row + 1):
                    for j in range(min_col, max_col + 1):
                        if len(table[i][j]) == 2:
                            (r11, c11, r22, c22), *_ = table[i][j]
                            min_row = min(min_row, r11)
                            max_row = max(max_row, r22)
                            min_col = min(min_col, c11)
                            max_col = max(max_col, c22)
                # update the value
                value = 'EMPTY'
                if table[r2][c2] != 'EMPTY':
                    value = table[r2][c2]
                    if len(value) == 2:
                        value = value[-1]
                if table[r1][c1] != 'EMPTY':
                    value = table[r1][c1]
                    if len(value) == 2:
                        value = value[-1]
                # merge
                for i in range(min_row, max_row + 1):
                    for j in range(min_col, max_col + 1):
                        table[i][j] = [(min_row, min_col, max_row, max_col), value]

        elif cmd == 'UNMERGE':
            r, c = map(int, info)
            if len(table[r][c]) == 2:
                (r1, c1, r2, c2), value = table[r][c]
                for i in range(min(r1, r2), max(r1, r2) + 1):
                    for j in range(min(c1, c2), max(c1, c2) + 1):
                        table[i][j] = 'EMPTY'
                table[r][c] = value

        else:
            r, c = map(int, info)
            # already merged
            if len(table[r][c]) == 2:
                value = table[r][c][-1]
            # not merged
            else:
                value = table[r][c]
            while values[value] != '':
                value = values[value]
            result.append(value)

        # for i in range(1, 5):
        #     for j in range(1, 5):
        #         print(table[i][j], end=' ')
        #     print()
        # print()
    return result
