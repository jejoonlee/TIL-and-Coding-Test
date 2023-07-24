package sample2;
public class Car extends Automobile{
    public String name = "car";
    public int engine;

    public Car(double maxSpeed, int seatNum, String name, int engine) {
        super(maxSpeed, seatNum);
        this.name = name;
        this.engine = engine;
    }
}
