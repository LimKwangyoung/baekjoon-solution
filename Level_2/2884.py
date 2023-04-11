H, M = map(int, input().split())

if M >= 45:
    print(f'{H} {M - 45}')
else:
    print(f'{(H + 23) % 24} {(M + 15) % 60}')