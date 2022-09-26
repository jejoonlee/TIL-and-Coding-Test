import sys
sys.stdin = open('input.txt')

# 알파벳 2개가 2개씩 있어야 Yes
# 먼저 set으로 다른 알파벳들이 몇 개가 있는지 확인
  # 만약 알파벳이 2개가 아니면 바로 No를 출력
# 그리고 알파벳이 2개인데, 하나라도 동일한 알파벳이 2개가 있으면 참
  # 알파벳 총 4개 중 다른 알파벳이 2개가 있는데, 동일한 알파벳이 2개가 있다면, 다른 알파벳도 2개가 있는 것

T = int(input())

for t in range(1, T + 1):
  word = list(input())
  word_cnt = set(word)

  if len(word_cnt) != 2:
    print(f'#{t} No')
  
  else:
    for w in word_cnt:
      if word.count(w) == 2:
        print(f'#{t} Yes')
        break