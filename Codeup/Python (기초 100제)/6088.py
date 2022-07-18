a, d, n = map(int, input().split())

result = a + d * (n - 1)    # 이미 a부터 시작하기 때문에, n번째에서 1을 뺀다

print(result)