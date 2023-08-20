import java.util.*;

class Solution {
    public static int solution(String[] ingredients, String[] items) {
        int answer = 0;
        int left = 0;
        int right = items.length - 1;

        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for (int i = 0; i < ingredients.length; i++) {
            if (map.containsKey(ingredients[i])) {
                int num = map.get(ingredients[i]);
                map.put(ingredients[i], num + 1);
            } else {
                map.put(ingredients[i], 1);
            }
        }

        while (true) {
            if (!map.containsKey(items[left]) && map.containsKey(items[right])) {
                left++;
            } else if (map.containsKey(items[left]) && !map.containsKey(items[right])) {
                right--;
            } else if (!map.containsKey(items[left]) && !map.containsKey(items[right])) {
                left++;
                right--;
            } else {
                HashMap<String, Integer> tempMap = new HashMap<String, Integer>();

                for (int i = left; i <= right; i++) {
                    if (map.containsKey(items[i]) && tempMap.containsKey(items[i])) {
                        int num = tempMap.get(items[i]);
                        tempMap.put(items[i], num + 1);
                    } else if (map.containsKey(items[i]) && !tempMap.containsKey(items[i])) {
                        tempMap.put(items[i], 1);
                    }
                }

                ArrayList<String> extra = new ArrayList<>();
                boolean isAnswer = true;

                for (String key : map.keySet()) {
                    if (map.get(key) < tempMap.get(key)) {
                        isAnswer = false;
                        extra.add(key);
                    }
                }

                if (isAnswer) {
                    answer = right - left + 1;
                    break;
                } else {
                    if (extra.contains(items[left])) {
                        left++;
                    } else if (extra.contains(items[right])) {
                        right--;
                    }
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] ingredients = {"생닭", "인삼", "소주", "대추"};
        String[] items = {"물", "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"};

        int result = solution(ingredients, items);
        System.out.println("Maximized Value: " + result);
    }
}