package personJava;

public class Educator extends Person {

    public String school;
    public Educator(String name, long num, String school) {
        super(name, num);
        this.school = school;
    }

    @Override
    public void getInfo() {
        System.out.println("Educator Class");
        System.out.println(super.name + " " + super.num + " " + this.school);
    }

}
