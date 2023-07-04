# [Java] 알고리즘 이진 탐색





#### 이진 탐색은 정렬된 데이터에서 특정 데이터를 빠르게 찾는 방법이다



![img](https://blog.kakaocdn.net/dn/FzF4h/btrWIP861l1/YNTPdtd9kdghl9kzk1OZSK/img.png)



- 데이터를 정렬을 한다
- 정렬 후, 중간 인덱스를 찾고, 해당 값이, 구하려는 값과 같은 값인지 본다
- 찾으려는 값이 더 작다면, 중간 인덱스 기준 왼쪽으로 / 크다면 중간 인덱스 기준으로 오른쪽으로 탐색을 한다
- 위와 같이 왼쪽 또는 오른쪽 기준에서 중간 지점을 찾고, 중간에 있는 숫자보다 작은지 큰지, 또는 같은지 탐색을 한다
- 그리고 숫자 하나가 남을때까지 탐색을 한다 (마지막 숫자 하나가 답이 아니면, 찾으려는 숫자가 없는 것이다)



```java
// ========== loop문으로 구현 =================

public static int binarySearch(int[] array, int target) {
    int left = 0;
    int right = array.length - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (array[mid] == target) {
            return mid;
        } else if (target > array[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}


// ========== 재귀로 구현 =================

public static int binarySearchRe(int[] array, int target, int left, int right) {
    if (left > right) {
        return -1;
    }

    int mid = (left + right) / 2;
    if (target > array[mid]) {
        return binarySearchRe(array, target, mid + 1, right);
    } else if (target < array[mid]) {
        return binarySearchRe(array, target, left, mid - 1);
    } else {
        return mid;
    }
}

// ========= 내장 함수 ===========
import java.util.*;

public static void main(String[] args) {
    int[] array = {1, 2, 7, 8, 9, 11, 17, 21, 26, 27, 70, 77};

    System.out.println(Arrays.binarySearch(array,7));
    // output : 2
    System.out.println(Arrays.binarySearch(array,10));
    // output : -6

}
```



- 다행이도 Arrays.binarySearch() 를 이용하여 이진 탐색을 가지고 올 수 있다
- 배열과, 찾으려는 값을 넣으면 된다
- 값이 없을 때에는, 찾으려는 값이 어느 지점과 가까운지 반환을 해준다



