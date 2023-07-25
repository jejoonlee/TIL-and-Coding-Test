package personJava;

public class Person {
    public String name;
    public long num;

    public void getNum() {
        System.out.println(num);
    }

    public Person(String name, long num) {
        this.name = name;
        this.num = num;
    }

    public void getInfo() {
        System.out.println("Person Class");
        System.out.println(name + " " + num);
    }


}
