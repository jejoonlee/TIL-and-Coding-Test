# Pandas - Series



## Head and Tail

#### head()

- 기본은, 제일 위에서 부터, 5개의 데이터를 불러와 주는 것이다
- 괄호 안에, 데이터의 개수를 넣어, 원하는 만큼의 데이터를 불러올 수 있다

```python
import pandas as pd

pokemon = pd.read_csv("./pandas/pokemon.csv", usecols=["Pokemon"]).squeeze()

# 위에서부터 5개의 데이터 출력
pokemon.head()

# 위에서부터 3개의 데이터 출력
pokemon.head(3)

# 위에서부터 10개의 데이터 출력
pokemon.head(10)
```





#### tail()

- 기본은, 제일 밑에서 부터, 5개의 데이터를 불러와 주는 것이다
- 괄호 안에, 데이터의 개수를 넣어, 원하는 만큼의 데이터를 불러올 수 있다

- 

```python
import pandas as pd

google = pd.read_csv("./pandas/google_stock_price.csv", usecols=["Stock Price"]).squeeze()

# 밑에서부터 5개의 데이터 출력
pokemon.tail()

# 밑에서부터 3개의 데이터 출력
pokemon.tail(3)

# 밑에서부터 10개의 데이터 출력
pokemon.tail(10)
```





## Copy vs View

> #### Copy 는 데이터를 완전히 복제하고, 복제한 데이터는 원본과 같지만, 독립적이다
>
> - A를 copy 하여, B를 만들었다
> - B를 수정한다고 A가 수정되지 않는다 (즉 처음에 A와 B의 데이터는 같지만, A와 B는 각각 독립적으로 행동을 한다)
>
> #### View 는 데이터 중에 특정 데이터를 보거나, 데이터 자체를 보는 것이다
>
> - A에서 B를 만드는 것이 아닌, A 안에 있는 데이터를 읽는 것





## Pandas에서 사용이 가능한 파이썬 함수

```python
import pandas as pd

pokemon = pd.read_csv("./pandas/pokemon.csv", usecols=["Pokemon"]).squeeze()

len(pokemon)		# pokemon의 데이터의 개수를 출력
# output : 721

type(pokemon)		# pokemon의 데이터 타입을 출력
# output : pandas.core.series.Series

dir(pokemon)		# pokemon에 사용할 수 있는 메서드 또는 함수 출력

sorted(pokemon)		# pokemon 데이터를 오름차순으로 정렬 (알파벳 또는 숫자), 리스트로 반환해준다

list(pokemon)		# pokemon을 리스트로 반환

dict(pokemon)		# pokemon을 딕셔너리로 반환

max(pokemon)		# 숫자는, 제일 큰 수를 출력, 문자는, 오름차순으로 정렬되었을 때, 마지막 단어 출력
# output : 'Zygarde'

min(pokemon)		# 숫자는, 제일 작은 수를 출력, 문자는, 오름차순으로 정렬되었을 때, 처음 단어 출력
# output : 'Abomasnow'
```



## sort_values

#### sorted() 을 사용하면, series를 리스트로 반환해준다

#### 반대로 그대로 series를 사용하되, 값들을 정렬하고 싶으면 sort_values()를 사용하면 된다



```python
import pandas as pd

pokemon = pd.read_csv("./pandas/pokemon.csv", usecols=["Pokemon"]).squeeze()

pokemon.sort_values()
# series를 반환하되, 값들을 오름차순으로 정렬한다

pokemon.sort_values(ascending=False)
# series를 반환하되, 값들을 내림차순으로 정렬한다
```



## sort_index

#### 인덱스를 정렬하고 싶을때 사용하는 메서드다



```python
import pandas as pd

pokemon = pd.read_csv("./pandas/pokemon.csv", index_col="Pokemon").squeeze()

pokemon..sort_index(ascending=False)
```

- index_col : 인덱스 행을 Pokemon으로 설정해준다
  - pokemon.csv 에는 Pokemon과 Type 행이 있어, 자연스럽게 Pokemon이 인덱스, Type이 값이 된다
- sort_index : 오름차순으로 인덱스를 정렬해준다
  - sort_index(ascending=False) : 내림차순으로 인덱스를 정렬해준다
