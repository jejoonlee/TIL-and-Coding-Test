import java.math.BigDecimal;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        int[] scores = {100, 90, 95, 60, 70};

        Student student = new Student("Alex", 100, 90, 95, 60, 70);
        int number = student.getNumberOfMarks();
        int sum = student.getTotalSumOfMarks();
        int maximumMark = student.getMaximumMark();
        int minimumMark = student.minimumMark();
        BigDecimal average = student.getAverageMarks();

        System.out.println(average);
        System.out.println(minimumMark);

        student.addNewMark(24);

        System.out.println(student.toString());

    }
}