def all_substrings(s):
    subs = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subs.append(s[i:j])
    return subs

# Example
print(all_substrings("abc"))  # ['a', 'ab', 'abc', 'b', 'bc', 'c']
