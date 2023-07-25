package personJava;

public class Main {
    public static void main(String[] args) {

        Person p1 = new Person("Els", 1234);
        Educator teacher = new Educator("joon", 1234, "high school");

        p1.getInfo();
        teacher.getInfo();
    }
}