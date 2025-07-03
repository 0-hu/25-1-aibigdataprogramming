N, M = map(int, input().split())

# # num = input().split()
# # N, M = map(int, num)

print(N // M) if N > M else print(M // N)
print(N % M) if N > M else print(M % N)

# div, mod = divmod(N,M) if N > M else divmod(M,N)
# print(f'{div}\n{mod}')