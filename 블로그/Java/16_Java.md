# 16. Java Array







## Array가 필요한 이유

> #### 여러 변수를 만들어서, 각 변수마다 값을 저장하는 것보단, 변수 하나를 만들어 Array에 값들을 저장할 수 있다
>
> - 똑같은 변수에 이름만 다르게 해서, 값들을 저장하는 것보단, 하나의 변수에 값들을 저장하는 것이 더 효율적이다
> - 그리고 Array는 순회가 가능해서, 찾고자 하는 값을 순회를 하며 찾으면 된다



```java
jshell> int[] marks2 = new int[5];
marks2 ==> int[5] { 0, 0, 0, 0, 0 }

jshell> int[] marks = {1, 2, 3};
marks ==> int[3] { 1, 2, 3 }

jshell> marks2[0] = 5;
$3 ==> 5

jshell> marks2
marks2 ==> int[5] { 5, 0, 0, 0, 0 }

jshell> marks2.length
$5 ==> 5
```

- **int[] marks2 = new int[5];**
  - marks2에 새로운 array를 넣고, array 안에 들어가는 원소는 5개이다

- **int[] marks = {1, 2, 3};**
  - marks라는 새로운 array를 만들고, 안에는 1, 2, 3 이라는 3개의 원소가 들어간다
- **.length 는, array의 원소 개수를 출력해준다**



#### array의 index는 0부터 시작한다



### 그 외의 자료형 Array

```java
jshell> double[] values = new double[5];
values ==> double[5] { 0.0, 0.0, 0.0, 0.0, 0.0 }

jshell> boolean[] boolValues = new boolean[5];
boolValues ==> boolean[5] { false, false, false, false, false }

jshell> class Person{
   ...> }
|  created class Person

jshell> Person[] persons = new Person[6];
persons ==> Person[6] { null, null, null, null, null, null }
```





### Array를 출력하기

```java
jshell> int[] marks = {1, 2, 3, 4, 5}
marks ==> int[5] { 1, 2, 3, 4, 5 }

// marks가 저장되어 있는 메모리의 위치를 출력해준다
jshell> System.out.println(marks);
[I@2d38eb89

jshell> System.out.println(Arrays.toString(marks))
[1, 2, 3, 4, 5]
```





### Arrays.fill(), Arrays.equals(), Arrays.sort()

```java
jshell> int[] marks = new int[5];
marks ==> int[5] { 0, 0, 0, 0, 0 }

jshell> Arrays.fill(marks, 100);

jshell> marks
marks ==> int[5] { 100, 100, 100, 100, 100 }

jshell> int[] array1 = {1, 2, 3};
array1 ==> int[3] { 1, 2, 3 }

jshell> int[] array2 = {1, 2, 3};
array2 ==> int[3] { 1, 2, 3 }

jshell> Arrays.equals(array1, array2)
$21 ==> true
```



##### Arrays.fill(배열 이름, 넣을 값)

- 배열 안에, 모든 원소를, 넣을 값으로 채워준다



##### Arrays.equals(배열 1, 배열 2)

- 두 배열을 비교한다 (배열 안에 원소의 개수와, 모든 원소의 값이 같을 때만 true를 반환한다)



##### Arrays.sort(배열)

- 배열을 정렬해준다





#### for문으로 탐색하기

```java
for (int mark: studentMarks) {
	answer += marks;
}

for (int i = 0 ; i < studentMarks.length; i ++) {
    answer += studentMarks[i];
}
```

- 첫 번째는, 원소를 하나씩 빼서, 더해주는 구조다
  - 쓰는 것도 편하고, 읽기도 편하다
- 두 번째는 인덱스를 가지고, 원소를 찾아서 더해주는 for문이다
  - 인덱스를 가지고 값을 찾는 것이기 때문에, 활용도는 더 높을 것이다



