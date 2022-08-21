# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

# N이 9 이고, 9개의 점수가 아래와 같이 주어질 경우,
# 85 72 38 80 69 65 68 96 22
# 69이 중간값이 된다.


N = int(input())
num = list(map(int, input().split()))
# N은 정수의 개수이고
# num은 중간값을 구할 정수들을 리스트 안에다 넣어 둔 것이다

num_sort = sorted(num)
# sorted(num)을 통해 num (리스트)에 있는 정수들을 오름차순으로 정렬한다

mid = int(N / 2)
# mid는 구해서 중간값이 몇 번째인지 구한다
# 2로 바로 나눈 이유는 리스트의 인덱스는 0부터 시작하기 때문이다

result = num_sort[mid]
# result 변수는 정렬된 num_sort의 mid번째의 인덱스이다

print(result)