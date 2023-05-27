# 15. Java Wrapper 클래스, Dates





## Wrapper 클래스란?

> #### Wrapper : Boolean, Byte, Character, Double, Float, Integer, Long, Short
>
> #### Primitive : boolean, byte, char, double, float, int, long, short



#### 위에 보이는 것 같이 Wrapper 클래스는 Primitive 값을 감싸준다

- Wrapper 클래스는, 다양한 옵션을 제공해준다
- Wrapper만에 메서드가 있다



#### 아래는 Integer 위주로 사용하지만, 다른 Wrapper 클래스들도 사용이 가능하다



```java
jshell> Integer integer = new Integer(5);
integer ==> 5

jshell> integer
integer ==> 5

jshell> Integer integer = Integer.valueOf(4);
integer ==> 4
    
jshell> Integer integer = new Integer("523");
integer ==> 523
```

- Wrapper 클래스를 사용해서, 변수를 만들는 방법들이다



```java
jshell> Integer i1 = new Integer(5);
i1 ==> 5

jshell> Integer i2 = new Integer(5);
i2 ==> 5

jshell> Integer i3 = Integer.valueOf(5);
i3 ==> 5

jshell> Integer i4 = Integer.valueOf(5);
i4 ==> 5

jshell> i1 == i2
$43 ==> false

jshell> i3 == i4
$44 ==> true
```

- **i1 == i2** 가 **false** 인 이유
  - 처음부터, 새로운 변수에 새로운 값을 저장을 했다
  - 5와 5는 같은 값이지만, 완전히 다른 변수의 값으로 나눠진다 (새로운 객체를 지속적으로 만드는 것)
- **i3 == i4** 가 **true** 인 이유
  - 똑같은 값의 변수가 있는지 확인을 한다
  - 똑같은 값의 변수가 있으면, 그 변수의 값을 가져와서 사용한다
  - 즉 5라는 숫자는 하나의 변수를 통해서 전파되어, 같은 값으로 인식이 된다 (같은 객체를 이용하는 것)





### Auto Boxing

```java
jshell> Integer i = Integer.valueOf(5);
i ==> 5
    
jshell> Integer i = 5;
i ==> 5
```

- **Integer i = Integer.valueOf(5);** 와 **Integer i = 5;** 는 똑같은 것이다
  - Auto Boxing을 통해 코드는 짧아졌고, **Integer i = 5;**를 하면, **.valueOf()**를 해줘서, 반복되는 객체가 있는지 확인 후, 값을 변수에 저장해준다





## Dates

> #### Dates도 datatype, 자료형 중 하나다



```java
jshell> import java.time.*

jshell> LocalDateTime DateTime = LocalDateTime.now();
DateTime ==> 2023-05-27T16:03:11.974813

jshell> LocalDate timeNow = LocalDate.now();
timeNow ==> 2023-05-27

jshell> LocalTime localTimeNow = LocalTime.now();
localTimeNow ==> 16:03:43.631642100
```

- **LocalDateTime DateTime = LocalDateTime.now();**
  - 날짜와 시간
- **LocalDate timeNow = LocalDate.now();**
  - 날짜
- **LocalTime localTimeNow = LocalTime.now();**
  - 시간



```java
jshell> LocalDate today = LocalDate.now();
today ==> 2023-05-27

// ----오늘 날짜에 대한 정보----
jshell> today.getYear();
$53 ==> 2023

jshell> today.getDayOfWeek()
$54 ==> SATURDAY

jshell> today.getDayOfMonth()
$55 ==> 27

jshell> today.getDayOfYear()
$56 ==> 147
    
jshell> today.getMonth()
$57 ==> MAY

jshell> today.getMonthValue()
$58 ==> 5

// ----년도, 월에 대한 정보----
jshell> today.isLeapYear()
$59 ==> false

jshell> today.lengthOfYear()
$60 ==> 365

jshell> today.lengthOfMonth()
$61 ==> 31
    
// ---- 몇일, 몇개월, 몇년 후 날짜 ----
jshell> today.plusDays(100)
$62 ==> 2023-09-04

jshell> today.plusMonths(100)
$63 ==> 2031-09-27

jshell> today.plusYears(100)
$64 ==> 2123-05-27
    
// ---- 빼기도 가능 ----
jshell> today.minusYears(40)
$65 ==> 1983-05-27
```

- 시간도 빼기, 더하기, 그 외에 시간에 대한 정보도 받을 수 있다



#### Date도 변수의 값이 바뀌지 않는다





### 오늘 말고 다른 날 구하기

```java
jshell> LocalDate yesterday = LocalDate.of(2023, 05, 26);
yesterday ==> 2023-05-26

jshell> today
today ==> 2023-05-27

jshell> today.withYear(2016)
$68 ==> 2016-05-27

jshell> today.withDayOfMonth(20)
$69 ==> 2023-05-20

jshell> today.withMonth(3)
$70 ==> 2023-03-27

jshell> today.withDayOfYear(120)
$71 ==> 2023-04-30
    
// 날짜를 비교할 수 있다
jshell> today.isBefore(yesterday)
$72 ==> false

jshell> today.isAfter(yesterday)
$73 ==> true
```



