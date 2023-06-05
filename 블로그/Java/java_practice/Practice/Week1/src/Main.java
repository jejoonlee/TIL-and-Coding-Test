
import java.util.Scanner;
import java.util.Date;
import java.util.Random;
import java.time.*;

public class Main {
    public static void main(String[] args) {
        class Website {}
        class Google extends Website {}

        Website website = new Google();
        // Google google = new Website(); 는 불가능 하다

        System.out.println(website instanceof Website);
        System.out.println(website instanceof Google);


    }
}