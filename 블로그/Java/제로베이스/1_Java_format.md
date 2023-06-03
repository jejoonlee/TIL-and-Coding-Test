# [TIL] Java (String.format())

*출처 : 제로베이스 백엔드 스쿨*





## String.format()

#### 문자열로 포멧을 하여 반환을 하는 것이다

- **%d** : 10진수, 정수 형태를 포멧하는 것이 
- **%s** :  문자열을 포멧하는 것이고, 숫자를 입력할 경우, 그만큼 빈 공간을 추가해준다
- **%f** : float 숫자를 문자열 형태로 포멧을 할 수 있다
- **%t** : 날짜시간 형식을 문자열 형태로 포멧할 수 있다
- **%c** : 유니코드 문자 형식을 문자열 형태로 포멧할 수 있다
- **%o, %x** : 8진수, 16진수를 문자열 형태로 포멧하는 것이다

```java
int num = 12;

System.out.println(String.format("%d", num));
// output : 12

System.out.println(String.format("%04d", num));
// output : 0012

System.out.println(String.format("%d____", num));
// output : 12____

System.out.println(String.format("%d04", num));
// output : 1204

System.out.println(String.format("%dd", num));
// output : 12d

System.out.println(String.format("%daaaa____", num));
// output : 12aaaa____

System.out.println(String.format("%d!!&#*&", num));
// output : 12!!&#*&

System.out.println(String.format("654d", num));
// output : 654d
```

- **"%04d"** : 해당 숫자가 4자리 수가 아니면, 앞에 0을 4자리 수가 만들어 질만큼 채워 준다





### %s

```java
String str = "hello";

System.out.println(String.format("%s", str));
// output : hello

System.out.println(String.format("%4s", str));
// output :     hello

System.out.println(String.format("%s____", str));
// output : hello____

System.out.println(String.format("%s04", str));
// output : hello04

System.out.println(String.format("%ss", str));
// output : hellos

System.out.println(String.format("%saaaa____", str));
// output : helloaaaa____

System.out.println(String.format("%s!!&#*&", str));
// output : hello!!&#*&
```

- **"%04s"** : 이 형식은 문자열에서는 에러가 뜬다





### %f

```java
double num = 12345.6789;

System.out.println(String.format("%f", num));
// output : 12345.678900

System.out.println(String.format("%.1f", num));
// output : 12345.7

System.out.println(String.format("%.2f__", num));
// output : 12345.68__

System.out.println(String.format("%015.2f__", num));
// output : 000000012345.68__

System.out.println(String.format("%f04", num));
// output : 12345.67890004
```

- 기본을 소수 6자리 수까지 출력을 해준다
- **"%.1f"** : 소수 1번째 자리 수까지 출력해준다
- **"%015.2f__"** : 소수 2번째 자리 수까지 출력해주지만, 총 자리 수가 15개가 안 되면, 앞에 0으로 채워준다





### %t

- 날짜, 시간은 뒤에 추가로 알파벳을 붙여야 한다

```java
Date date = new Date();

System.out.println(String.format("년도월일 : %tF", date));
// output - 년도월일 : 2023-06-02

System.out.println(String.format("연도 : %tY", date));
// output - 연도 : 2023

System.out.println(String.format("월 : %tm", date));
// output - 월 : 06

System.out.println(String.format("월 : %tB", date));
// output - 초 : 6월

System.out.println(String.format("일 : %td", date));
// output - 일 : 02

System.out.println(String.format("시간 : %tT", date));
// output - 시간 : 11:22:34

System.out.println(String.format("시 : %tH", date));
// output - 시 : 11

System.out.println(String.format("분 : %tM", date));
// output - 분 : 22

System.out.println(String.format("초 : %tS", date));
// output - 초 : 34
```



### %c

- 숫자를 유니코드로 반환

```java
System.out.println(String.format("48 → %c, 57 → %c", 48, 57));
// ouput : 48 → 0, 57 → 9

System.out.println(String.format("65 → %c, 90 → %c", 65, 90));
// ouput : 65 → A, 90 → Z

System.out.println(String.format("97 → %c, 122 → %c", 97, 122));
// ouput : 97 → a, 122 → z
```





### %s, %o, %h, %x

```java
int num = 217;

System.out.println(String.format("10진수 : %d" ,num));
// ouput - 10진수 : 217

System.out.println(String.format("2진수 : %s" , Integer.toBinaryString(num)));
// ouput - 2진수 : 11011001

System.out.println(String.format("8진수 : %o" ,num));
// ouput - 8진수 : 331

System.out.println(String.format("16진수 : %h" ,num));
// ouput - 16진수 : d9

System.out.println(String.format("16진수 : %x" ,num));
// ouput - 16진수 : d9
```

