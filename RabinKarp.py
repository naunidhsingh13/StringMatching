
def RabinKarpMethod(text: str, pattern: str, base: int = 10, modulo: int = 2**31):

    m, n = len(pattern), len(text)

    pattern_hash_value = 0
    text_hash_value = 0
    for i in range(m):
        pattern_hash_value += ord(pattern[i])*base**(m-1-i) % modulo
        text_hash_value += ord(text[i])*base**(m-1-i) % modulo

    result = []
    i = 0
    while True:
        if text_hash_value == pattern_hash_value and text[i:i+m] == pattern:
            result.append(i)

        if i + m >= n:
            break

        text_hash_value -= ord(text[i])*base**(m-1) % modulo
        text_hash_value *= base
        text_hash_value += ord(text[i+m]) % modulo

    return result




