# [Spring] WebClient



#### 처음에는 외부 API를 통해서 JSON 파일로 파싱을 해서 데이터를 가지고 왔다



#### RestTemplate이라는 라이브러리를 추천 받았다

- 하지만, Spring 문서에서는 Spring 5.0에서부터는 RestTemplate보다는 WebClient를 사용하라고 권고하고 있다



> NOTE: As of 5.0 this class is in maintenance mode, with only minor requests for changes and bugs to be accepted going forward. Please, consider using the org.springframework.web.reactive.client.WebClient which has a more modern API and supports sync, async, and streaming scenarios.



#### 그래서 WebClient를 한번 사용해보기로 했다

- WebClient는 비동기 처리가 가능하여, 대규모 데이터 처리 및 대기 시간이 있는 API 경우 유용하다고 해서, WebClient를 사용했다





#### 1. build.gradle

- webflux 의존성을 추가한다

```
// WebClient 사용
implementation 'org.springframework.boot:spring-boot-starter-webflux'
```





#### 2. TMDB에서 영화 장르 가지고 오기

- **WebClient.builder()** 를 통해서 기본적인 WebClient 객체를 가지고 온다
  - baseUrl : 기본 URL
  - **codecs(configurer -> configurer.defaultCodecs().maxInMemorySize(-1))**
    - **DataBufferLimitException: Exceeded limit on max bytes to buffer : 262144 에러**
    - 위와 같은 에러가 떠서 codecs를 추가했다 (여기서 -1 은 unlimited 이다)
- **webClient.get()** : get 메서드를 통해서 TMDB에서 영화 장르를 가지고 온다
  - uri 에 장르에 관련된 uri와 파라미터를 추가해준다
  - header 에, apikey가 필요함으로 apikey를 넣어준다
  - retrieve().bodyToMono() 에서는 원하는 리턴 클래스를 명시해준다
    - 즉 TMDB에서 제공해주는 데이터 위주로 응답할 클래스를 만들면 된다

```java
@RequiredArgsConstructor
@Service
public class MovieExternalApiClient {
    
    private static final WebClient webClient = WebClient.builder()
            .baseUrl("https://api.themoviedb.org/3")
            .defaultHeader(HttpHeaders.ACCEPT, "application/json")
            .codecs(configurer -> configurer.defaultCodecs().maxInMemorySize(-1))
            .build();

    static MovieExternalApiDto.GenreList getGenre(String apiKey, String language) {

        MovieExternalApiDto.GenreList response = webClient.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/genre/movie/list")
                        .queryParam("language", language)
                        .build())
                .header(HttpHeaders.AUTHORIZATION, apiKey)
                .retrieve()
                .bodyToMono(MovieExternalApiDto.GenreList.class)
                .block();

        return response;
    }
}
```



#### 3. 응답할 클래스

- 여기서 중요한 것은, API에서 제공해주는 데이터 이름, 그대로 가지고 와야 한다!
- '_' 이 있으면 그대로 써야 한다.
  - 캐멀 케이스로 시도해보았지만 모두 null을 리턴했

```java
public class MovieExternalApiDto {

    @Getter
    @Setter
    public static class GenreList{
        private List<Genre> genres;
    }

    @Getter
    @Setter
    public static class Genre{
        private Long id;
        private String name;
    }
}
```



