# 📋 Web Pair Project

🚨🚨  **[Code Link](https://github.com/jejoonlee/webpjt-0210)** 🚨🚨

**Category**

- [index](#index)
- [community](#community)



## 후기

전체적으로 Bootstrap을 거의 모든 요소에 사용을 했다. 

두번째 그룹 프로젝트고, 처음으로 페어로 프로젝트를 했는데, 첫번째 그룹 프로젝트 때보다 더 몰입도가 있었다.

특히 상대방이 모르는 것이 있으면, 알려주면서 나 자신도 복습을 할 수 있었고, 같이 찾아보면서 많이 배울 수 있었다.

얘기를 하면서 프로젝트를 진행하니, 속도는 조금 느렸지만, 그래도 재미있게 할 수 있었다.



## index

![home 결과물](README.assets/home 결과물.gif)

- 로그인에 Modal을 이용한 것이 제일 새로웠다.
  - Modal 안에 로그인 정보를 넣는데, submit 버튼과 위에 로그인 정보를 연결하는데 집중을 했다.
    - 결국 submit 버튼을 로그인 정보 (Form) 태그 안에 넣어 문제를 해결했다
- 그 외에는 그전에 경험을 해서, 많이 익숙했던 부분들이었다

> my role : navigator
>
> 최대한 많이 알려주려고 했다. 대신 직접적으로 코드를 알려주는 것보단, 무엇을 어떻게 했으면 좋겠다라고 많이 얘기를 했었다.
>
> 특히 파트너분이 잘 하셔서, 큰 어려움은 없었다. 오히려 편하게, 어떤 요소를 넣으면 좋을지 얘기를 많이 했던 것 같다.





## community

![community 결과물](README.assets/community 결과물.gif)

- `media query` 를 이용해야 했었다
  - 992px 미만일 때에 table이 없어지고 card가 나와야 했고
    - `@media (max-width: 992px)` 
      - 최대 992px까지는 table이 `display: none`을 통해 없어지고
      - 카드가 나와 있다
  - 992px 이상일 때에 table이 나타나고 card가 나와야 했다
    - `@media (min-width: 992px)` 
      - 992px부터 cards들이 `display: none`을 통해 없어지고
      - 테이블이 나온다
  - html 상, table과 cards 들은 존재하지만, 화면 사이즈에 따라, 없어지거나, 나타나게 된다



