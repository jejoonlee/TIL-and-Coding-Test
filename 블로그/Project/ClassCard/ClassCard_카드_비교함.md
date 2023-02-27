# 클래스 카드 - 카드 비교

![bg-img](ClassCard_intro.assets/bg-img.png)





## 카드 비교 모델 (Model)

```python
class CompareCard(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
```

- 로그인을 해야 카드 비교 기능을 사용할 수 있다
  - 그래서 유저 정보를 가지고 오고, `card` 정보를 통해서 카드를 `카드 비교함`에 넣는 것이다
  - 여기서 `user`마다 카드는 최대 3개까지 `카드 비교함`에 넣을 수 있다



## 카드 비교함에 카드 넣기 (요청)

![image-20230226190334678](ClassCard_카드_비교함.assets/image-20230226190334678.png)

```python
# 카드를 비교하기 위해서 비교하기 바구니에 넣고 / 비교하기 페이지
path('bookmark/<int:pk>/', views.bookmark, name="bookmark"),
path('card_compare/', views.card_compare, name="card_compare"),
```

- `비교함에 추가`를 누르면 `bookmark/<int:pk>`를 명령하게 된다
  - 여기서 `<int:pk>`는 카드의 ID 값이다



<img src="ClassCard_카드_비교함.assets/image-20230226190444787.png" alt="image-20230226190444787" style="zoom:50%;" />

- `카드 비교 보러가기` 버튼은 `card_compare/` 페이지로 넘어갈 수 있도록 한다



## 기능 구현

```python
@login_required(login_url='/login/')
def bookmark(request,pk):

    user = request.user
    card = Card.objects.get(pk=pk)
    not_work = True
    compare_add = True

    compare_bag = []

    if user.is_authenticated:
        user_bookmark = CompareCard.objects.filter(user = user)
        
        # CompareCard에 해당 유저 내용이 없으면, 바로 유저와 카드를 저장한다
        if len(user_bookmark) == 0:
            compare_add = True
            compare = CompareCard(user=user, card=card)
            compare.save()
        
        else:
            # 유저가 저장한 카드 내용들을 bookmark_card에 저장한다
            bookmark_card = []
            for bookmark in user_bookmark:
                    bookmark_card.append(bookmark.card)

            if 0 < len(bookmark_card) <= 3 :
                # 같은 카드가 있는지 확인하고, 있으면 지워버린다

                if card in bookmark_card:
                    compare_add = False
                    card_ind = bookmark_card.index(card)
                    user_bookmark[card_ind].delete()

                else:
                    # 3개까지 카드를 저장할 수 있다
                    if len(bookmark_card) + 1 != 4:
                        compare_add = True
                        compare = CompareCard(user=user, card=card)
                        compare.save() 
                    else:
                        not_work = False
                        messages.warning(request,'카드 3개까지 추가가 가능합니다! 비교함에서 카드를 꺼내주세요 ㅜ.ㅜ')
                        pass

            else:
                not_work = False
                messages.warning(request,'카드 3개까지 추가가 가능합니다! 비교함에서 카드를 꺼내주세요 ㅜ.ㅜ')
    else:
        pass

    
    cardcard = CompareCard.objects.filter(user=user)

    for card in cardcard:
        compare_bag.append({
            "cardId" : card.card.id,
            "cardName": card.card.card_name,
            "cardImg": card.card.card_img,
        })

    data = {
        "compareBag" : compare_bag,
        "compareAdd" : compare_add,
        "notWork" : not_work,
    }

    return JsonResponse(data)
```



- 비교함의 기능은, 기본적으로 `if`문이 많이 들어간다
  - 만약 이미 카드 비교함에 카드가 3개로, 가득차면, 더 이상 카드를 추가할 수 없다
  - 같은 카드를 두 번 누르면, 없어지게 만든다
    - 예) XXXX 하나 카드의 `비교함에 추가`를 한번 누르면, 카드 비교함에 추가된다
    - XXXX 하나 카드의 `비교함에 추가`를 한번 더 누르면, 카드 비교함에서 빠지게 된다





## Template 구현

#### 카드 비교 기능은 기본적으로 모든 페이지에 들어가야 한다

- 즉, base.html에 이 기능을 넣었다
- 이렇게 함으로써, 모든 페이지에서 `카드 비교`를 눌렀을 때에, 카드 비교함, 즉 모달 창을 볼 수 있게 된다
