


B, N = input().split(' ')
N = int(N)

answer = 0
for i in range(len(B) - 1, -1, -1):
    num = len(B) - i - 1
    letterNum = ord(B[i])

    if 65 <= letterNum <= 90:
        answer += N ** num * (letterNum - 55)
    elif 49 <= letterNum <= 57:
        answer += N ** num * (letterNum - 48)

print(answer)