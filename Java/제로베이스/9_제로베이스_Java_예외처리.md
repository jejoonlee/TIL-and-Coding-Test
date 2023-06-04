# [제로베이스] Java 예외 처리

*출처 : 제로베이스 백엔드 스쿨*





## 예외 처리

#### 프로그램을 실행했을 때에, 오류가 발생하는 일이 있다

#### 이 오류를 미리 예측하고, 오류가 발생했을 때에 특정 코드를 진행 시킬 수 있도록 한다



### try, catch, finally

```java
try {
    실행 코드;
} catch (예외 이름 1) {
    실행 코드에서 '예외 이름 1' 이 발생했을 때에 실행 할 코드;
} catch (예외 이름 2) {
    실행 코드에서 '예외 이름 1' 이 발생했을 때에 실행 할 코드;
} finally {
    예외가 발생하든 말든, 실행되는 코드;
}
```



### throw, throws

- **throw** : 예외를 발생 시킨다
- **throws** : 예외를 전가 시킨다



```java
// =========== throw ================
함수 () {
    throw new Exception();
}

try {
    throw new Exception();
} catch (Exception e) {
    System.out.println("예외를 발생시켰습니다")
}

// =========== throws ================
함수 () throws Exception {
    
}

// 예외가 발생하면, 함수 내에서 예외를 처리하는 것이 아니라,
// 함수 밖에서 예외를 처리해준다
checkTen (int x) throws NoTenException {
    if (x != 10) {
        new throw NoTenException();
    }
    return true;
}

// 그래서 아래와 같이 함수를 다시 호출하고,
// try 문에서 예외를 처리해준다
try {
    checkTen(5);
} catch (NoTenException e) {
    System.out.println(e + ": This is not 10";)
}
```

