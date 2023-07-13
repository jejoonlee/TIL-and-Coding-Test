import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

class Phone {
    public String phoneNo;
    public String phoneOwner;
    public String phoneName;

    Phone(String phoneNo, String phoneOwner, String phoneName) {
        this.phoneNo = phoneNo;
        this.phoneOwner = phoneOwner;
        this.phoneName = phoneName;
    }

    public void call() {
        System.out.println("Calling");
    }
}

public class Practice4 {
    public static void main(String[] args) {
        Phone phone = new Phone("01049288537", "이제준", "Note 20");

        System.out.println(phone.phoneNo);
    }
}
