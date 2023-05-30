import java.math.BigDecimal;
import java.util.ArrayList;

public class Student {
    private String studentName;
    private ArrayList<Integer> studentMarks = new ArrayList<Integer>();

    public Student (String name, int... marks) {
        this.studentName = name;
        for (int mark: marks) {
            this.studentMarks.add(mark);
        }
    }

    public int getNumberOfMarks() {
        return studentMarks.size();
    }

    public int getTotalSumOfMarks() {
        int markSum = 0;
        for (int mark : studentMarks) {
            markSum += mark;
        }
        return markSum;
    }

    public int getMaximumMark() {
        int maxMark = 0;
        for (int mark: studentMarks) {
            if (mark > maxMark) {
                maxMark = mark;
            }
        }
        return maxMark;

        // return Collections.max(studentMarks);
    }

    public int minimumMark() {
        int minMark = 100;
        for (int mark: studentMarks) {
            if (mark < minMark) {
                minMark = mark;
            }
        }
        return minMark;

        // return Collections.min(studentMarks);
    }

    public BigDecimal getAverageMarks() {
        BigDecimal allScore = new BigDecimal(getTotalSumOfMarks());

        return allScore.divide(new BigDecimal(studentMarks.size()));
    }

    public void addNewMark(int value) {
        this.studentMarks.add(value);
    }

    public void removeMarkAtIndex(int index) {
        this.studentMarks.remove(index);
    }

    public String toString() {
        return studentName + studentMarks;
    }
}
