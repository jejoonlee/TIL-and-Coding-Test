# Joontooling 프로젝트

> 업무 : 회원가입 모델링





## Daum 주소 API 가지고 오기

```html
<label for="address">주소</label>
<div class="signup-field">
    {% render_field form.address class="input_effect" placeholder="주소" id="address" %}
    <button onclick="searchAddress()">도로명 주소 찾기</button>
</div>

<p>상세 주소를 추가해 주세요</p>
```

- 주소 입력칸 그리고 주소 찾기 버튼을 만든다
- 주소 찾기 버튼을 누르면 Daum 주소 찾기 팝업을 띄운다



```html
<script src="//t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
<script>

  function searchAddress() {
    new daum.Postcode({
        oncomplete: function(data) {
          
          // 도로주소
          roadAddress = data.roadAddress;

          document.getElementById("address").value = roadAddress;
        }
    }).open();
  }
</script>
```

- Daum 주소 찾기 API는 따로 Key를 받지 않아도 된다
- 위에 있는 코드를 그냥 가지고 오면된다
- 예제 코드가 있는데, 예제 코드보다는 간단하게 만들어서 사용했다



`function searchAddress()` : 함수이다. HTML에서 `주소 찾기 버튼`을 누르면 `<button onclick="searchAddress()">`을 통해서 searchAddress 기능을 실행시켜 준다 (즉 팝업을 띄어준다)



Daum에서 제공해주는 속성은 많았지만 `roadAddress` 속성만 사용했다. (도로명 주소)



`roadAddress = data.roadAddress;`을 통해서 도로명 주소의 데이터를 받는다.



`document.getElementById("address").value = roadAddress;` 

- 여기서 `address` ID는 HTML에는 주소 입력창이다. (`{% render_field form.address class="input_effect" placeholder="주소" id="address" %}`)
- 입력창에 `roadAddress` 값을 넣어준다.
- 그렇게 하면, 도로주소가 바로 입력창에 보이게 된다.

