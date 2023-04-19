# 📋Python 좌표계



#### 좌표계는 동근 지구를 2차원 평면에 투영하는 다양한 방법이다



#### 주로 위도, 경도 (Latitude, Longitude)를 사용한다

- 대표적으로  **ESPG:4326 / WGS84** 이 있다



#### 하지만, 한국에서 사용하는 특정 데이터에서, x와 y를 통해 위치를 찾는 것을 볼 수 있게 되었다

- 이것을 **ESPG:5181** 이고 카카오나 공공데이터포탈에서 자주 사용한다



#### 개인적으로는 위도, 경도가 익숙해서, 공공데이터포탈에서 가지고 온 x,와 y 좌표를 위도와 경도로 변환하는 방법을 찾았다



#### 아래는 pyproj 버전이 업데이트 하기 전이다

```python
from pyproj import Proj, transform

epsg5181= Proj(init="epsg:5181")
wgs84=Proj(init='epsg:4326')

longitude,latitude =  transform(epsg5181, wgs84,item['엑스좌표_값'],item['와이좌표_값'])
```



#### pyproj 버전이 업데이터가 된 후, 코드가 더 간단해 졌다

```python
from pyproj import Transformer

transformer = Transformer.from_crs("epsg:5181", "epsg:4326")

lat, long = transformer.transform(y값, x값)
# y값, x값

print(lat, long)
```

- Transformer를 사용하여 **epsg:5181** 을 **epsg:4326** 으로 변환하는 것이다
