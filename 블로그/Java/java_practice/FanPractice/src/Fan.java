public class Fan {

    // state (상태)

    private String make;
    private double radius;
    private String color;
    private Boolean isOn = false;
    private int speed;

    // constructor
    Fan (String make, double radius, String color) {
        this.make = make;
        this.radius = radius;
        this.color = color;
    }

        // Behavior (행동)

    public void switchOn() {
        this.isOn = true;
        this.speed = 10;
        System.out.println("The fan is on: " + this.isOn);
    }

    public void switchOff() {
        this.isOn = false;
        this.speed = 0;
        System.out.println("The fan is on: " + this.isOn);
    }

    public void setSpeed(int speed) {
        this.speed = speed;
        System.out.println("The Speed is now " + this.speed);
    }
}
