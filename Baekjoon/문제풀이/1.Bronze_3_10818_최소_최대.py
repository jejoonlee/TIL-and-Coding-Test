# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())

inp = list(map(int, input().split()))
# inp는 int로 변환된 값들을 list 안에 넣는 것이다

print(min(inp), max(inp))