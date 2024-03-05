def temp(a, b):
    M = max(a, b)+25
    m = min(a, b)*2

    return M, m

a, b = map(int, input().split())

M, m = temp(a, b)
print(f"{M} {m}")