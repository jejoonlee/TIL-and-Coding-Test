# 🧑‍💻 Gradebook Project

> Project using list
>
> You are a student and you are trying to organize your subjects and grades using Python



```python
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']
grade = [98, 97, 85, 88]

gradebook = [
  ['physics', 98],
  ['calculus', 97],
  ['poetry', 85],
  ['history', 88]
]

# adds 'computer scienc'e and 'visual arts' to 'gradebook'
gradebook.append(['computer science', 100])
gradebook.append(["visual arts", 93])


gradebook[-1][-1] = 98

# Changes poetry class's score from 85 to 'Pass'
gradebook[2].remove(85)
gradebook[2].append('Pass')
# [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]

full_gradebook = gradebook + last_semester_gradebook
# joins two list together
# [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98], ['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65]]

print(full_gradebook)
```

