# [TIL] Java (LocalDate)

*출처 : 제로베이스 백엔드 스쿨*





## LocalDate

> #### import java.time.*
>
> - 시간 관련된 모든 클래스를 가지고 올 수 있다
> - LocalDateTime, LocalDate, DayOfWeek 등



```java
import java.time.*;

// 현재 날짜, yyyy-mm-dd
LocalDate nowDate = LocalDate.now();

// 1996년 2월 17일에 대한 날짜
LocalDate date = LocalDate.of(1996, 2, 17);

// =========현재 날짜를 출력하기==============
System.out.println(nowDate);
//	output : 2023-06-02

// =========현재 년도를 출력하기==============
System.out.println(nowDate.getYear());
//	output : 2023

// =========올해 몇일이 있는지 출력하기==============
System.out.println(nowDate.lengthOfYear());
//	output : 365

// =========윤년인지 확인==============
System.out.println(nowDate.isLeapYear());
//	output : false

// =========몇 월인지 출력==============
System.out.println(nowDate.getMonth());
//	output : JUNE

// =========몇 월인지 숫자로 출력==============
System.out.println(nowDate.getMonthValue());
//	output : 6

// =========현재 달의 일 수==============
System.out.println(nowDate.lengthOfMonth());
//	output : 30

// =========현재 달에서 몇일인지 출력==============
System.out.println(nowDate.getDayOfMonth());
//	output : 2

// =========현재 요일 출력==============
System.out.println(nowDate.getDayOfWeek());
//	output : FRIDAY

// ==========현재 날짜에서 10일 더하기==============
System.out.println(nowDate.plusDays(10));
//	output : 2023-06-12

// =========현재 날짜에서 10개월 더하기==============
System.out.println(nowDate.plusMonths(10));
//	output : 2024-04-02

// ==========현재 날짜에서 10주 추가하기==============
System.out.println(nowDate.plusWeeks(10));
//	output : 2023-08-11

// ==========현재 날짜에서 10년 추가하기==============
System.out.println(nowDate.plusYears(10));
//	output : 2033-06-02

// ==========현재 날짜에서 10일 빼기==============
System.out.println(nowDate.minusDays(10));
//	output : 2023-05-23

// ==========현재 날짜에서 10주 빼기==============
System.out.println(nowDate.minusWeeks(10));
//	output : 2023-03-24

// ==========현재 날짜에서 10개월 빼기==============
System.out.println(nowDate.minusMonths(10));
//	output : 2022-08-02

// ==========현재 날짜에서 10년 빼기==============
System.out.println(nowDate.minusYears(10));
//	output : 2013-06-02

// =====현재 날짜와 date 날짜를 비교하기 (년도 차이)====
System.out.println(nowDate.compareTo(date));
//	output : 27
```



#### 이 외에도 LocalDateTime도 비슷하게 적용할 수 있다

- LocalDateTime은 시간까지 알려준다

```java
LocalDateTime nowDateTime = LocalDateTime.now();

System.out.println(nowDateTime);
// output : 2023-06-02T16:09:07.227

System.out.println(nowDateTime.getHour());
// output : 16

System.out.println(nowDateTime.getMinute());
// output : 9

System.out.println(nowDateTime.getSecond());
// output : 7
```



