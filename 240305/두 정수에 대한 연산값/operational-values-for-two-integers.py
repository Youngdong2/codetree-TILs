def temp(a, b):
    M = max(a, b)+25
    m = min(a, b)*2

    print(f"{m} {M}")

a, b = map(int, input().split())
temp(a, b)