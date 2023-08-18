# 스프링 Initializer

*출처 : 제로베이스 백엔드 스쿨*



#### 스프링 프로젝트를 실행할 때에, 기본적인 틀을 Spring Initializr 웹사이트, 또는 IDE에서 만들 수 있다

- https://start.spring.io/





## 프로젝트

#### Maven Project / Gradle Project

- 스프링의 빌드 관리 도구다
- 빌드 관리 도구는, 라이브러리를 관리해주고, 자바로 코딩한 프로젝트를 빌드 및 실행을 도와주는 주체이다
  - 그 중에 Maven과 Gradle, 최신 빌드 관리 도구다
- Gradle이 더 최신 것이다 (새로 만드는 프로젝트는 주로 Gradle로 만들다)





## Language

#### 프로그래밍 언어를 선택하는 것이다



#### 익숙한 언어를 선택하면 된다!

- **Java, Kotlin, Groovy**
  - Kotlin과 Groovy는 Java에서 파생된 언어다





## Spring Boot (스프링 버전)

#### Snapshot : 새 기능이 포한 된 버전 (조금 불안정하다)

- 검증이 되지 않은 버전



#### M (Milestone) : Snapshot을 조금 더 정리한 버전



#### 괄호가 없는 버전 : 정식으로 배포된 버전

- 안정적이라서, 혹시 모를 버그나 에러를 피할 수 있다
  - Snapshot과 M이 있어도 버그나 에러가 없을 수도 있지만, 테스트를 덜 했기 때문에, 확실하지 않다





## Project Metadata

#### Group : 보통 일하고 있는 회사 도메인을 넣어준다

- 개인은 블로그 도메인을 사용하는 사람들도 있다



#### Artifact : 프로젝트 이름



#### Name, Description, Package Name : 자동으로 입력이 된다



#### Packaging

- **JAR (Java Archive)**
  - 서버만 만들 때에, JAR만 선택해도 큰 문제가 없다
- **WAR  (Web Application Archive)** : 웹 관련된 자원을 포함한다
  - WAR는 JAR에서 추가적인 웹 관련 요소를 넣을 때에 필요하다
  - 예시) HTML, JS 파일을 추가적으로 넣을 때 WAR를 선택하는 것이 좋다



#### Java : 버전

- 무조건 최신 버전을 사용한다고 좋은 것이 아니다
- 8, 11, 17 버전은 LTS (Long Time Support)
  - LTS : 장기간 지원해주는 버전
  - **2023년 8월 기준 (End Of Support Life)**
    - Java 17 : 2029년 9월
    - Java 11 : 2026년 9월
    - Java 8 : 2030년 12월





## Dependency

#### 스프링에서 사용할 라이브러리 (추후에 프로젝트 중에 따로 설정할 수 있다)

- 카테고리 별로 제시해주고 있다
- 예) Developer Tools, Web, SQL, NoSQL 등



#### Lombok : 코드를 간결해준다

- 반복적으로 작성하는 코드를 간결하게 사용할 수 있도록 만들어주는 라이브러리다



#### Spring Web : Rest API를 만들 때 필요한 라이브러리
