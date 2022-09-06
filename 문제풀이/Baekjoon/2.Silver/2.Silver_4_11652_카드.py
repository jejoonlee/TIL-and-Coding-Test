import sys
sys.stdin = open('input.txt', 'r')

qty = int(input())

card = {}
nums = []

for q in range(qty):
    num = input()
    nums.append(num)

for number in nums:
    if number not in card:
        card[number] = 1
    else:
        card[number] += 1

max_value = max(card.values())

most_card = []
for key, value in card.items():
    if value == max_value:
        most_card.append(key)

print(min(map(int, most_card)))