# Udemy : Python 블랙잭 프로젝트

> #### 카드를 뽑아서, 카드의 숫자들을 더해서 21 이하로 맞추는 것이다
>
> #### 21 이상이고, 상대방이 21 이하이면, 무조건 지는 것이다
>
> #### 상대방과 비교해서, 둘 다 21 이하일 때, 21과 제일 가까운 숫자가 이기는 것이다

- J, Q, K = 10
- A = 1 또는 11
- 2~10은 각자 주어진 번호

##### 첫 카드는 공개이다

##### 공개를 했는데, 17 이하이면, 무조건 추가 카드를 받아야 한다

```python
import random
from replit import clear
from art import logo

def deal_card():
  """returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
flag = True

while play_game == 'y':
  clear()
  print(logo)
  user_card = []
  computer_card = []
  
  for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
  
  print(f"Your cards: {user_card}, current score: {sum(user_card)}")
  print(f"Computer's first card: {computer_card[0]}")

  continue_game = input("Type 'y' to get another card, type 'n' to pass:")

  while continue_game == 'y':
    user_card.append(deal_card())

    if sum(user_card) > 21:
      if 11 in user_card:
        user_card[user_card.index(11)] = 1
      else:
        flag = False
        break
    
    print(f"Your cards: {user_card}, current score: {sum(user_card)}")
    print(f"Computer's first card: {computer_card[0]}")
    continue_game = input("Type 'y' to get another card, type 'n' to pass:")

  while sum(computer_card) <= 17:
    computer_card.append(deal_card())

  print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
  print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
  
  if flag == False:
      print("You've been busted!. You lose")
  else:
    if sum(computer_card) > 21:
      print("Computer's busted. You win!")
    elif sum(computer_card) > sum(user_card):
      print("You lose!")
    elif sum(computer_card) == sum(user_card):
      print("You draw")
    else:
      print("You win!")

  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
```

#### 설명

- 게임을 시작한다는 입력 'y' 를 하면 게임을 시작한다
  - 한 게임이 끝나도 'y'를 입력하면, 게임을 계속 할 수 있다
- 먼저 `user_card`와 `computer_card` 리스트에 카드 2장씩 랜덤으로 넣는다
- user에게 카드를 뽑고 싶은지 물어본다
  - 여기서 'y'를 뽑게 되고, 만약에 21이 넘으면 while문을 정지시키고 flag를 False로 만들어서, 게임에서 졌다고 출력을 한다
  - 유저의 카드들이 21이 넘었지만, 유저가 11 즉 Ace를 가지고 있으면 1로 반환해준다
    - Ace는 11 또는 1 이다
- 컴퓨터도 가지고 있는 카드가 17 이하면, 계속 카드를 뽑아야 한다
- 그리고 최종적으로 `user_card`와 `computer_card` 각각의 카드들을 더하고, 21이하 면서, 상대방보다 합이 더 크면 이기게 된다



