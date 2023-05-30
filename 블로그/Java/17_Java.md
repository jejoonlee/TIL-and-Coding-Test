# 17. Java Array, ArrayList





## 가변적 매개변수 (Variable Arguments)

```java
// 1번
Student student = new Student("Alex", new int[] {97, 81, 100});

// 2번
Student student = new Student("John", 88, 77, 100, 66);
```

- 1번처럼, 2개의 arguments를 클래스에 넣어서 객체를 만들 수 있다
  - 이 때에 입력할 수 있는 argument는 고정이 되어 있다
- 2번 같은 경우, 숫자들은 모두 점수이다
  - 여기서는 클래스에 입력할 수 있는 argument의 개수가 고정이 아니다



#### 고정적인 argument보다는, 다양한 값을 클래스에 넣고 싶을 때에 가변적 매개변수를 사용한다

```java
public int sum (int... values) {
    int answer = 0;
    for (int value: values) {
        answer += value;
    }
    return answer
}
```

- **int... values**
  - **...** 을 넣으면, argument를 제한 없이 넣을 수 있다
  - 여기서 **...** 을 사용하게 되면 array로 만들어준다





## ArrayList

> #### 한번 Array가 만들어졌으면, 새로운 원소를 추가하거나, 뺄 수 없다



#### Array에 원소를 추가할 때에

- 임시 Array를 만들어, 추가할 원소와, 원래 기존의 원소들을 for문을 통해 넣어준다
- 그리고 임시 Array를 기존 Array에 덮어씌운다

```java
int[] nums = {1, 2, 3, 4};
// nums ==> int[4] { 1, 2, 3, 4 }

int[] temp_nums = new int[nums.length + 1];
// temp_nums ==> int[5] { 0, 0, 0, 0, 0 }

for (int i = 0; i < nums.length; i++) {
    temp_nums[i] = nums[i];
}
// temp_nums ==> int[5] { 1, 2, 3, 4, 0 }

temp_num[nums.length] = 5;
// temp_nums ==> int[5] { 1, 2, 3, 4, 5 }

nums = temp_nums;
// nums ==> int[5] { 1, 2, 3, 4, 5 }
```





#### ArrayList 사용하기

```java
jshell> ArrayList<String> items = new ArrayList<String>();
// items ==> []

jshell> items.add("Football");
jshell> items.add("Basketball");
jshell> items.add("Rugby");

jshell> items
// items ==> [Football, Basketball, Rugby]

jshell> items.remove("Rugby");

jshell> items.remove(1);

jshell> items
// items ==> [Football]
```

- **.add()** 와 **.remove()** 를통해서, 리스트에 있는 원소를 삭제할 수 있다
  - **.remove()** 는 원소 값 또는 인덱스를 사용할 수 있다





#### Array에서 ArrayList로 바꾸기

- Array를 for문으로 순회를 하면서 ArrayList에 넣기 (지금까지 배운 것 기준)
