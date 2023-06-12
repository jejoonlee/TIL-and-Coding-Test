# [제로베이스] Java 컬렉션 프레임워크

*출처 : 제로베이스 백엔드 스쿨*



## List 프레임워크

#### 인덱스로 데이터의 위치를 알 수 있고, 여러 개의 데이터가 들어가 있다

#### ArrayList / Linked List / Vector 등이 있다



### ArrayList

```java
ArrayList arrayList = new ArrayList();

// 리스트 안에 데이터 넣는 방법
arrayList.add(7);
arrayList.add(8);
arrayList.add(9);

// 리스트 안에 인덱스가 2인 값을 삭제한다
arrayList.remove(2);
// 리스트 안에 값이 9인 값을 삭제한다
arrayList.remove(Integer.valueOf(9));

arrayList.size(); // 리스트 크기

arrayList.indexOf(7); // 7인 값의 인덱스 찾기

arrayList.contains(9); // 9가 리스트 안에 있는지 확인하기
```



### Linked List

- Python에서 deque 처럼 활용할 수 있는 것 같다

```java
LinkedList linkedList = new LinkedList();

// 추가, 삭제, 크기, 확인 등은 ArrayList 처럼 할 수 있다

// 제일 앞과 제일 뒤에 데이터를 넣거나 삭제할 수 있다
linkedList.addFirst(6);
linkedList.addLast(10);

linkedList.removeFirst();
linkedList.removeLast();
```





## Set 프레임워크

#### 데이터 관련 순서가 없다

#### 중복된 데이터를 집어 넣지 못 한다

- 7을 2개 넣으려고 해도, 7 하나만 들어가 진다

#### HashSet / TreeSet 등이 있다



```java
// =========== HashSet ===========
HashSet set1 = new HashSet();

// 추가하기
set1.add(7);
set1.add(8);
set1.add(9);

// 삭제하기, 인덱스가 없어, 값을 넣으면 된다
set1.remove(9);

set1.size();
set1.contains(7);

// =========== TreeSet ===========
TreeSet set2 = new TreeSet();

set2.add(7);
set2.add(8);
set2.add(9);

// 삭제하기, 인덱스가 없어, 값을 넣으면 된다
set2.remove(9);

set2.size();
set2.contains(7);

// 제일 처음에 있는 데이터
set2.first();

// 제일 마지막에 있는 데이터
set2.last();

// 8보다 큰 데이터
set2.lower(8);

// 9보다 큰 데이터
set2.higher(8);

// 전체 데이터를 삭제한다
set2.clear();
```







## Map 프레임워크

#### Key, Value 이 들어가 있다

#### HashMap / TreeMap



```java
// ========== HashMap ==============
HashMap hashMap = new HashMap();
hashMap.put(1, "Man Utd");
hashMap.put(2, "Liverpool");
hashMap.put(3. "Arsenal");

// key 값을 넣으면 된다
hashMap.remove(2);
hashMap.get(1);


// ========== TreeMap ============
TreeMap treeMap = new TreeMap();
treeMap.put(1, "Man Utd");
treeMap.put(2, "Liverpool");
treeMap.put(3. "Arsenal");
treeMap.put(4, "Tottenham");

// key 값을 넣으면 된다
treeMap.remove(2);
treeMap.get(1);

// 제일 앞에 있는 값의 Key
treeMap.firstKey();
// output : 1

// 제일 앞에 있는 값의 key, value
treeMap.firstEntry();
// output : 1=Man Utd

treeMap.lastEntry();
// output : 3=Arsenal

treeMap.lastKey();
// output : 3

treeMap.lowerEntery(3);
// output : 1=Man Utd

treeMap.higherEntery(3);
// output : 4=Tottenham
```





