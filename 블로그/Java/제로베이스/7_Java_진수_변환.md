# [TIL] Java (진수 변환)





## 10진수 => 16진수 or 8진수 or  2진수 변환

- **Integer.toBinaryString(십진수)** 
  - 10진수에서 2진수로 변환
- **Integer.toOctalString(십진수)** 
  - 10진수에서 8진수로 변환 
- **Integer.toHexString(십진수)** 
  - 10진수에서 16진수로 변환



```java
public class Main {
    public static void main(String[] args) {
        int number = 77;

        System.out.println(Integer.toBinaryString(number));
        // output : 1001101
        System.out.println(Integer.toOctalString(number));
        // output : 115
        System.out.println(Integer.toHexString(number));
        // output : 4d

    }
}
```







## 16진수 or 8진수 or  2진수 변환 => 10진수 변환



- **Integer.parseInt(문자열, radix)**

  - 문자열만 넣게 된다면, 숫자로 이루어진 문자열을 정수로 반환해준다
  - radix를 추가하게 되면, 문자열에 있는 숫자를 해당 숫자로 넣은 진수를 인식해서 정수로 반환해준다
    - radix가 2면, 2진수 / 8이면 8진수 / 16이면 16진수다

  

```java
public class Main {
    public static void main(String[] args) {
        String binary = "1001101";
        String octal = "115";
        String hex = "4d";

        System.out.println(Integer.parseInt(binary, 2));
        // output : 77
        System.out.println(Integer.parseInt(octal, 8));
        // output : 77
        System.out.println(Integer.parseInt(hex, 16));
        // output : 77
    }
}
```





## AND, OR, XOR 연산자 사용하여 2진수 연산을 하고 십진수로 변환하기

- 2진수가 문자열로 주어지면, 먼저 2진수를 십진수로 반환한다
- AND, OR, XOR 연산자는 Integer만 사용할 수 있고, 반환된 십진수를 연산자를 통해 결과값을 반환한다
- 결과값은 십진수로 나와있다

```java
public class Main {
    public static void main(String[] args) {
        String bin1 = "1011010";
        String bin2 = "1101001";

        // 연산자를 사용하기 위해서 이진수를 십진수로 바꿔야 한다
        int num1 = Integer.parseInt(bin1, 2);
        int num2 = Integer.parseInt(bin2, 2);

        // AND, OR, XOR 연산자를 활용해서 2진수 연산을 하며 십진수를 출력한다
        System.out.println(num1 & num2);
        // output : 72
        System.out.println(num1 | num2);
        // output : 123
        System.out.println(num1 ^ num2);
        // output : 51
    }
}
```





## AND, OR, XOR 연산자 사용하여 2진수 연산을 하고 이진수로 변환하기

- 위의 결과를 이진수로 반환하기 위해서는 .**toBinaryString()** 을 이용하면 된다
- 여기서 따로 연산자를 사용하기 위해서는 **String.valueOf(num1 & num2);** 를 사용하면 된다

```java
public class Main {
    public static void main(String[] args) {
        String bin1 = "1011010";
        String bin2 = "1101001";

        // 연산자를 사용하기 위해서 이진수를 십진수로 바꿔야 한다
        int num1 = Integer.parseInt(bin1, 2);
        int num2 = Integer.parseInt(bin2, 2);

        int num1AndNum2 = Integer.parseInt(String.valueOf(num1 & num2));
        int num1OrNum2 = Integer.parseInt(String.valueOf(num1 | num2));
        int num1XorNum2 = Integer.parseInt(String.valueOf(num1 ^ num2));

        // AND, OR, XOR 연산자를 활용해서 2진수 연산을 하며 십진수를 출력한다
        System.out.println(Integer.toBinaryString(num1AndNum2));
        // output : 1001000
        System.out.println(Integer.toBinaryString(num1OrNum2));
        // output : 1111011
        System.out.println(Integer.toBinaryString(num1XorNum2));
		// output : 110011
    }
}
```

