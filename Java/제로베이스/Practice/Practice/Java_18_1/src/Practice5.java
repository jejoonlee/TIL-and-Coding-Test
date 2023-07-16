
public class Practice5 {
    public static int solution(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        int maxWater = 0;

        while (left < right) {
            int lowWall = Math.min(height[left], height[right]);
            int water = 0;

            for (int i = left; i <= right; i ++) {
                water += Math.min(lowWall, height[i]);
            }

            if (water > maxWater) {
                maxArea = (right - left) * lowWall;
                maxWater = water;
            }

            if (height[left] < height[right]) {
                left ++;
            } else {
                right --;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        // Test code
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(solution(height));

        height = new int[]{5, 3, 9, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2};
        System.out.println(solution(height));

    }
}
