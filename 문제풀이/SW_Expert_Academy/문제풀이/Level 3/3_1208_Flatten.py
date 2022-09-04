import sys
sys.stdin = open('input.txt')

# while문 말고 for문으로 풀어보기
# 실행시간이 확실히 for문이 더 빠르다!
# while문을 쓰면 180ms
# for문을 쓰면 150ms

# 1. 박스가 제일 높은 곳에 있는 박스를 제일 낮은 위치에 올려 놓기
# 2. 1번이 한번의 dumping
# 3. 이걸 N번을 한다
# 4. N번이 끝나면, 마지막에 박스가 제일 높은 것과, 제일 낮은 차이를 구하는 것

for t in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    # N번을 반복
    for _ in range(N):
        highest = max(boxes)
        lowest = min(boxes)

        H = boxes.index(highest)
        L = boxes.index(lowest)

        # 덤핑 하기 (1번)
        boxes[H] -= 1
        boxes[L] += 1

    print(f'#{t} {max(boxes) - min(boxes)}')