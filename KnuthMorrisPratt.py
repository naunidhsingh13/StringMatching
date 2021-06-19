
def CreatePiTable(pattern: str):

    m = len(pattern)
    pi_table = [0]*m
    i, j = 0, 1
    prefix_len = 0
    while j < m:
        if pattern[i] == pattern[j]:
            prefix_len += 1
            pi_table[j] = prefix_len
            i += 1
            j += 1
        elif i != 0:
            i = 0
            prefix_len = 0
        else:
            j += 1

    return pi_table


def KMP_StringMatching(text: str, pattern: str):

    m, n = len(pattern), len(text)
    result = []

    pi_table = CreatePiTable(pattern)
    i, j = 0, 0

    while i < n:

        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                result.append(i-m)
                j = pi_table[j-1]

        elif j == 0:
            i += 1
        else:
            j = pi_table[j-1]

    return result
