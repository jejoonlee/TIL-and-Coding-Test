# 산메 (산책 메이트) - 지도 구현기능

![logo](Sanme_intro.assets/logo.png)



### 지도 기능 설명

- 공공 데이터 포털에서 도시공원 정보를 CSV 파일로 다운로드 받았다
  - 받고 난 후, 로컬 DB에 저장을 하여 공원 정보와 카카오 map API를 연결시켰다
- '내 위치'를 누르면, 현재 내가 있는 주소의 IP 주소를 트래킹하여 나의 위치를 가지고 온다
  - 그 위치를 기반으로 5km 반경에 있는 공원들을 표시한다
- 공원 검색 기능은, 공원 이름 또는 주소 기반으로 검색을 한다
  - 검색을 하면 내 위치로 기본적으로 이동하고, 내 위치에서 제일 가까운 순으로 나열이 된다
- 공원 마커 클릭
  - 마커를 클릭하게 된다면 마커 위에 해당 공원에 대한 정보가 간략하게 나온다
  - 그리고 마커에서 '산책하기' 를 클릭하면, 해당 공원의 좌표와 함께 `산책하기 모집` 생성 페이지로 간다

[![지도시연](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/%EC%A7%80%EB%8F%84%EC%8B%9C%EC%97%B0.gif)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/지도시연.gif)



### Kakao Map API 에서 공원 가지고 오기 (HTML & JavaScript)

> Kakao Map API에서 친절하게 설명을 해줘서, 크게 문제되는 것은 없다

[![semi2](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2.png)

[![semi2_2](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_2.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_2.png)



### 내 위치 기능 w/ 5km 반경 공원들

> views.py에서 내 위치에서 5km 반경엔 있는 공원들을 찾아서 Json 파일로 JavaScript로 보낸다
>
> Javascript로 데이터를 처리하는 속도가 데이터가 너무 많게 되면, 속도가 많이 느려진다
>
> 그래서 python으로 데이터를 왠만해서 많이 처리한 후, Javascript으로 마커를 표시하기만 했다
>
> #### 📌 **내 위치를 가지고 올 때에는, 내 위치를 찾았을 때와 못 찾았을 때의 상황을 가지고 와야 한다**
>
> - 내 위치를 가지고 오는 코드는 `navigator.geolocation.getCurrentPosition()` 이다

[![semi2_3](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_3.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_3.png)

[![semi2_4](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_4.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_4.png)

[![semi2_5](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_5.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_5.png)

[![semi2_6](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_6.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_6.png)





### 검색 기능

> 검색 기능도 내 위치 기능과 동일하다
>
> Python으로 데이터를 나눈 후, Javascript로 데이터를 나뉜 데이터들을 표시하게 끔 만들었다

[![semi2_7](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_7.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_7.png)

[![semi2_8](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_8.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_8.png)

[![semi2_9](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_9.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_9.png)

[![semi2_10](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_10.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_10.png)

[![semi2_11](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_11.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_11.png)

[![semi2_12](https://github.com/jejoonlee/TIL-and-Coding-Test/raw/master/Multicampus_Final_Project/Final_2.assets/semi2_12.png)](https://github.com/jejoonlee/TIL-and-Coding-Test/blob/master/Multicampus_Final_Project/Final_2.assets/semi2_12.png)
