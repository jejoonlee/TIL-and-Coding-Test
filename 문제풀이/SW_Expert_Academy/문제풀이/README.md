# ✍️ 알아두면 좋을 것 같은 것

#### 소수 구하기

```python
N = 100
cnt = 0

while cnt != N:
    cnt += 1
    divide = []
    for i in range(1, cnt + 1):
        if cnt % i == 0:
            divide.append(i)
    
    if len(divide) == 2:
        print(cnt)
    else:
        continue
```

- 100까지의 숫자 중에 소수 구하기
- 1부터 100까지 수를 순회한다.
- 순회하면서 1부터 해당 숫자 `cnt` 까지 나눈 후 나머지가 0이 되면 리스트에 따로 저장한다
- 리스트 길이가 2면 수소다