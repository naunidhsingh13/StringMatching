
def NaiveStringMatching(text: str, pattern: str):

    m, n = len(pattern), len(text)
    result = []

    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            result.append(i)

    return result
