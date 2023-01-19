# Udemy : Python 에니메이션과 좌표



## 뱀 게임

#### 자연스럽게 에니메이션 설정하기

```python
screen.tracer(0)
screen.update()
```

- 원래는 블록 하나씩 움직이는 것이 다 보였다
  - 하지만 블록 전체가, 하나로 움직이는 것을 보여야 한다
- `screen.tracer(0)`를 하면 동작 전체를 안 하도록 한다
- `screen.update()`를 하면, 하나의 `for문` 또는 묶여있는 동작이 실행이 되면, 한번에 동작을 블록 전체가 하나로 실행하게 보이게 된다 





#### 뱀 움직이기

![image-20230119091756781](19_Udemy_Python_뱀_게임.assets/image-20230119091756781.png)

```python
for snake_num in range(len(snake) - 1, 0, -1):
    new_x = snake[snake_num - 1].xcor()
    new_y = snake[snake_num - 1].ycor()
    snake[snake_num].goto(new_x, new_y)
```



#### 클래스화 시키기

![image-20230119100707841](19_Udemy_Python_뱀_게임.assets/image-20230119100707841.png)
