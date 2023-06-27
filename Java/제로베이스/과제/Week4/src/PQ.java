import java.util.*;


class Person{
    String name;
    int grade;

    Person(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }

//    @Override
//    public int compareTo(Person add) {
//        // 1 : 변경 안 함
//        // -1 : 변경 함
//
//        // 오름차순
//        return this.grade >= add.grade ? 1 : -1;
//
//        // 내림차순
////        return this.grade >= add.grade ? -1 : 1;
//    }
}
public class PQ {
    public static void main(String[] args) {
        String[] name = {"Alex", "Joon", "JayJay", "Green", "Houston", "Cesinha"};
        int[] grade = {3, 1, 5, 7, 2, 6};

        PriorityQueue<Person> pq = new PriorityQueue<Person>((Person p1, Person p2) -> p1.name.compareTo(p2.name));

        for (int i = 0; i < grade.length; i++) {
            pq.add(new Person(name[i], grade[i]));
        }

        for (Person person : pq) {
            System.out.println(person.name + " " + person.grade);
        }
    }
}