public class Student extends Person{
    private String schoolName;
    private int year;
    private String classNum;

    Student (String name, int age, String n, String a, String p, String sN, int y, String cN) {
        super(name, age, n, a, p);
        this.schoolName = sN;
        this.year = y;
        this. classNum = cN;
    }
}
