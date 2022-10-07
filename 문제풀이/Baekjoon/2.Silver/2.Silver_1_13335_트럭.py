import sys
sys.stdin = open('input.txt')

from collections import deque

n, w, L = map(int, input().split())

trucks = deque(list(map(int, input().split())))

queue = deque([0] * w)
cnt = 0
weight = 0

# 만약에 queue 안에 있는 트럭의 무게들 + trucks에 제일 앞에 있는 트럭의 무게
# 둘이 합했을 때에, 최대 하중보다 낮으면 trucks에 제일 앞에 있는 트럭을 queue에 넣는다

