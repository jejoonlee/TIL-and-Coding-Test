# Udemy : Python 퀴즈 프로젝트와 OOP의 장점



## 파이썬 클래스를 만드는 방법

> #### 클래스는 객체를 만들기 위한 블루프린트 (Blue Print)이다



```python
class User:
    pass

user_1 = User()
# 클래스를 불러올 때에는 클래스 이름 뒤에 ()를 붙인다
```

- `class User:`  -  class를 넣어주고, 뒤에 클래스의 이름을 쓰면된다
  - PascalCase - 클래스의 이름은 각 단어의 첫 번째 글자는 대문자로 써야 한다 (예) MyCar, UserInfo)
- `pass` - 클래스에 아무 정보를 넣고 싶지 않을 때



## 속성, 클래스 생성자, `__init__()` 함수 사용하기

![image-20230116095640192](16_Udemy_Python_퀴즈_프로젝트와_OOP의_장점.assets/image-20230116095640192.png)

```python
class User:
    
    def __init__(self, user_id, username):
        # initialise attributes / create starting value for attribute
        # called everytime class is called
        
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "Alex")
# 밑의 코드와 같다
# user_1.id = "001"
# user_1.username = "Alex"
```

- `followers` 같이, `__init__(self)`에 파라미터가 없으면, 객체를 만들때 들어가는 기본 값인 것이다
- **`self` 는 객체를 가리키는 것**



## 메소드 (Method) 추가하기

```python
class User:
    
    def __init__(self, user_id, username):
        # initialise attributes / create starting value for attribute
        # called everytime class is called
        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Alex")
user_2 = User("002", "Yang")

user_1.follow(user_2)
```

- 클래스 안에 function을 넣으면 된다
- `follow` 예시



## 퀴즈 프로젝트

> True Or False 게임이고, 맟추면 점수를 얻는 것

#### Main.py

```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append((Question(question['text'], question['answer'])))

question = QuizBrain(question_bank)

while question.still_has_question() == True:
    question.next_question()

    
print("You've completed the quiz")
print(f"Your final score was: {question.score}/{question.question_number}")
```

- 주요 기능들은 `main.py`에 썼다
- `main.py` 에 다른 파일에 있는 클래스들을 가지고 와서, 기능들의 코드를 짰다



#### brain_quiz.py

```python
class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: { current_question.text } (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("You got it wrong")
            
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
```





#### question_model.py

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```





#### data.py

```python
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
```

