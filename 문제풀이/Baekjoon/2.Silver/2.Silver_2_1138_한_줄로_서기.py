
import sys
sys.stdin = open('input.txt')


# 입력 받을 리스트와 입력받은 개수 만큼의 리스트를 만든다
# 여기서 중요한 것은 입력 받은 리스트들의 요소들은 앞에
# 0의 갯수라고 할 수 있다

N = int(input())

# 인덱스 + 1 이 키
see = list(map(int, input().split()))

result = [0] * N


for i in range(N):
  height = i + 1
  cnt = 0

  # result를 순회하기 위한 for문
  for j in range(N):
    
    # cnt가 see[i]와 같아질때까지
    # elif 문에서 cnt를 1씩 더한다
    if cnt == see[i]:
      if result[j] == 0:
        result[j] = height
        break
      else:
        continue
    
    # cnt가 1씩 누적되기 위해서는,
    # result를 순회할때 0을 만나야 한다
    elif result[j] == 0:
      cnt += 1

print(' '.join(map(str, result)))