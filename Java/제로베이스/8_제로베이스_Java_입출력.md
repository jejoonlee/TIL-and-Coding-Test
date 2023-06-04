# [제로베이스] Java 입출력, 정수/문자열 변환

*출처 : 제로베이스 백엔드 스쿨*





## 콘솔 입력

```java
// 하나의 char 만 출력해준다
// 입력을 받고, 출력을 하면, 2번째 코드도 작성해야 좋다
// 입력한 데이터 중, 하나만 출력할 수 있어, 남아있는 데이터를 없애는 코드다
System.in.read();
System.in.read(new byte[System.in.available()])

// 여러개의 데이터를 받을 수 있다
// 배열을 만들어야 한다 (즉 배열 사이즈에 따라서, 출력 크기가 달라진다)
InputStreamReader reader = new InputStreamReader(System.in);
char[] c = new char[5];
reader.read(c);

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String str = br.readline();

// 제일 많이 활용되는 방식이다
// System.in 은 콘솔로부터 입력을 받는 것이다
Scanner scanner = new Scanner(System.in);

int num = scanner.nextInt(); // 숫자를 입력
String str = scanner.next(); // 문자열을 입력
```





## 정수 문자열 변환

```java
int num = Integer.parseInt("12345");
String str = String.toString(12345);
```





## 콘솔 출력

```java
// 출력하고 한 칸 내려준다
System.out.println();

// 출력해주고, 이어준다
System.out.print();

// 포멧을 하며 출력해준다
System.out.printf();
```





## 파일 입력

```java
//======= FileWriter 사용 =============
FileWriter fw = new FileWriter("./test.txt");

// 글쓰기
String text = "Hello\n";
fw.write(text);

String text2 = "World\n";
fw.write(text2);

fw.close();

// 원래 파일에 추가로 쓰기
// 파일명 뒤에 true를 붙여주면 된다
FileWriter fw2 = new FileWriter("./test.txt", true);
String text3 = "!!!!";
fw.write(text3);
fw.close();

//======== PrintWriter ==============
PrintWriter pw = new PrintWriter("./test.text");

// 글쓰기
pw.println(text);
pw.println(text2);

pw.close();

// 원래 파일에 추가로 쓰기
PrintWriter pw2 = new PrintWriter(new FileWriter("./test.txt", true));
pw2.println(text3);
pw.close()
```





## 파일 출력

```java
BufferedReader br = new BufferedReader(new FileReader("./test.txt"));

while (true) {
    String line = br.readline();
    if (line == null) {
        break
    }
    System.out.println(line);
}

br.close;
