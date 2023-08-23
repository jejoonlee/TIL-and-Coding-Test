# 스프링 MVC

*출처 : 제로베이스 백엔드 스쿨*





## MVC 패턴

> #### Model, View, Controller
>
> - 역할 분담을 하기 위해 만든 패턴
> - Model : 로직 안에서 이동하고 있는 데이터
> - View : 화면 역할을 하는 것
> - Controller : 비즈니스 로직을 처리하고 모델과 뷰를 응답으로 준다



#### 일반적인 MVC 패턴



<img src="4_제로베이스_스프링.assets/0_Qf1s2lG86MjX-Zcv.jpg" alt="0_Qf1s2lG86MjX-Zcv" style="zoom:50%;" />







#### 스프링 MVC 패턴

- 유저가 요청을 보내면 **Dispatcher Servlet**을 통해 요청을 어디에 보낼지 **Handler Mapping** 통해 매핑을 한다
- 즉 **Dispatcher Servlet**은 **Handler Mapping**을 통해 역할 분담을 한다
- **Controller**에서 유저의 요청에 대한 요청 처리를 한다 

![flow-of-spring-web-mvc](4_제로베이스_스프링.assets/flow-of-spring-web-mvc.png)







## 스프링 MVC - HTTP 요청/응답



#### Controller / RestController

- Controller는 HTML을 응답값으로 한다
- RestController는 주로 JSON을 응답하고 Rest API에 대한 요청을 처리한다



#### 매핑 어노테이션

- **@RequestMapping** : Get 또는 POST 등, 요청 방식을 직접 한다
  - GET, HEAD, POST, PUT, PATCH, DELETE, OPTIONS, TRACE 메서드를 사용할 수 있다

```java
@RequestMapping(value="/index/1", method = RequestMethod.GET)
public String cls() {
    // 내용
}
```



#### 축약형 매핑 어노테이션

- **@GetMapping** : 데이터를 가져옴
- **@PostMapping** : 데이터를 전송
- **@PutMapping** : 전체 수정
- **@PatchMapping** : 일부 수정
- **@DeleteMapping** : 삭제



#### 파라미터에 요청 값 전송

- Get, Delete
  - **@PathVariable("id") String identity**
  - query-params : 추가적인 정보들 입력, 필터 페이징에서 많이 사용이 된다
    - **@RequestParam** : PathVariable과 동일하게 사용하면 된다
    - required 또는 defaultValue를 설정할 수 있다
    - required=false로 지정하면, 해당 파라미터에 입력값이 없어도 된다

```java
@GetMapping("/name/{nameId}")
public String getName(@PathVariable("nameId") String nameId) {
    // 로그에 출력이 된다
    log.info("Get name Id: " + nameId);
    return "nameId: " + nameId;
}
// http://localhost:8080/입력한ID

@GetMapping("/name")
public String getName(@RequestParam("nameId") String nameId) {
    // 로그에 출력이 된다
    log.info("Get name Id: " + nameId);
    return "nameId: " + nameId;
}
// http://localhost:8080/name?nameId=입력한ID
```



- **Post, Put, Patch** (url에 보이고 싶지 않을 때에)
  - **@RequestBody** : http body 정보를 편리하게 받을 수 있다 (주로 양이 많을 데이터를 받을 때)
    - JSON으로 메세지를 포멧 한다
  - **@RequestHeader** : http header 정보를 편리하게 받을 수 있다

