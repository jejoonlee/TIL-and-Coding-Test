public class GenericMethod {

    public static <T> void print(T[] value) {
        for(int i = 0; i < value.length; i ++) System.out.println(value[i]);
    }

    public static void main(String[] args) {
        String[] s = {"Hello", "My", "Name", "is", "Je Joon"};
        Integer[] i = {2, 3, 7, 9, 12, 13, 17};

        print(s);
        print(i);
    }

}
