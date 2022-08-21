H, M = map(int, input().split())

m = (H * 60 + M) - 45

wh = m // 60
wm = m % 60

if wh < 0:
    print(wh + 24, wm)
elif wh > 24:
    print(wh -24, wm)
else:
    print(wh, wm)
