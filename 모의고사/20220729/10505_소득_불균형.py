
T = int(input())

for t in range(1, T + 1):
    # 사람 인원
    num_ppl = int(input())
    # 소득을 정수 형태로 리스트에 넣기
    income = input().split()
    income = list(map(int, income))

    # 소득을 다 더하고, 인원으로 나누면 평균이 구해짐
    avg = sum(income) / num_ppl

    # 평균 소득보다 낮거나 같으면 리스트 안에 넣기
    low_income = []
    for i in income:
        if i <= avg:
            low_income.append(i)
    
    print(f'#{t} {len(low_income)}')