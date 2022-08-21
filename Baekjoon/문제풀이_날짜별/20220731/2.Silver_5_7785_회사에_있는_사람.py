
num = int(input())

log_list = {}

# 이름과 출퇴근 상태 입력
for i in range(num):
    logs = list(input().split())
    for log in logs:
        if log[0] not in log_list:
            log_list[logs[0]] = logs[1]
        elif log[0] in log_list:
            log_list[logs[0]] = logs[1]

enter = []
for key, value in log_list.items():
    if value == 'enter':
        enter.append(key)

final = sorted(enter, reverse = True)

for i in final:
    print(i)