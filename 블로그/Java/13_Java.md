# 13. Java Reference Types, 내장 String 클래스





## 메모리에 저장



### Reference Types

- 생성되는 모든 클래스가 Reference Type이다

```java
// planet은 reference type
class Planet {
    
}
```

- 그 외에 이미 자바에 만들어진 reference types는
  - String, BigDecimal 등이 있다



### Reference Variable

- 클래스를 토대로 만든 변수를 reference variable이라고 한다

```java
class Planet {
}

Planet jupiter = new Planet();
// 여기서 jupiter는 reference Variable이다
```

![image-20230523145505310](13_Java.assets/image-20230523145505310.png)

- reference variable은 힙에 저장이 된다
  - 더 나아가, 스택에는 value에는 메모리 공간이 저장이 되고, 변수 이름이 저장 된다
  - **즉, stack에는 reference variable이 힙의 메모리 공간의 경로를 표시한다**
- 반대로 primitive variable, 즉 기본 변수는, 스택에 저장된다







## String Class (String으로 저장된 변수 확인하기)



#### String은 클래스이고, 생성자가 필요가 없다

```java
BigDecimal bd = new BigDecimal("1.0");

String str = "Test";
```

- BigDecimal 같이 **new BigDecimal("1.0")**, 생성자가 필요 없이 바로 변수를 만들 수 있다



#### String은 인덱스가 0부터 시작한다

```java
String str = "Test";

str.charAt(0);
//output : 'T'

str.charAt(2);
//output : 's'

String biggerString = "This is a lot of text";
biggerString.substring(5);
//output : "is a lot of text"

biggerString.substring(5, 13);
//output : "is a lot"

biggerString.indexOf("lot");
//output : 10
```

- **A.charAt(인덱스)**
  - 해당 인덱스에 있는 단어, 또는 값을 반환해준다



- **A.substring(시작 인덱스, 미만 인덱스)**
  - 슬라이싱이 가능하다
  - 즉 특정 인덱스부터 반환해주거나, 반환하고 싶은 값의 인덱스의 범위를 지정해 줄 수 있다



- **A.length()**
  - 문자열의 길이를 반환해준다



- **A.indexOf("문자열")**
  - 입력한 문자열의 시작점의 인덱스를 반환해준다
  - 같은 문자가 있다면, 제일 처음에 등장하는 문자열의 인덱스를 반환해준다



- **A.lastIndexOf("문자열")**
  - 문자열을 넣었을 때, 중복되는 문자가 있을 수 있다
  - 그 중복되는 문자 중, 제일 마지막에 있는 문자의 인덱스를 반환해 준다



- **A.contains("문자열")**
  - **A** 안에, 해당 문자열이 있는지 확인해준다
  - true or false로 반환



- **A.startsWith("문자열")**
  - **A** 가 해당 문자열로 시작하는지 확인해준다
  - true or false로 반환



- **A.endsWith("문자열")**
  - **A** 가 해당 문자열로 끝나는지 확인해준다



- **A.isEmpty()**
  - **A** 가 비어 있는지 없는지 확인해준다



- **A.equals("문자열")**
  - **A** 가 해당 문자열과 같은지 확인해준다



- **A.equalsIgnoreCase("문자열")**
  - 대소문자를 무시한채로, **A** 와 문자열이 같은지 확인해준다

