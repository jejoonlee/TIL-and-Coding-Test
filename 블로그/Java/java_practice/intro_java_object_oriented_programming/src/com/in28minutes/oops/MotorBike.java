package com.in28minutes.oops;

public class MotorBike {
	
	// state
	private int speed;
	
	MotorBike(int speed) {
		this.speed = speed;
	}
	
	// behavior
	public void changeSpeed(int speed) {
		if (speed >= 0) {
			this.speed = speed;
		} else {
			System.out.println("This can not be a speed");
		}
	}
	
	int getSpeed() {
		return this.speed;
	}
	
	public void increaseSpeed(int speed) {
		if (speed >= 0) {
			changeSpeed(this.speed + speed);
		} else {
			System.out.println("You can only INCREASE speed");
		}
	}
	
	public void decreaseSpeed(int speed) {
		if (speed >= 0) {
			changeSpeed(this.speed - speed);
		} else {
			System.out.println("Negative value can not be an input");
		}
	}
	
	void start() {
		System.out.println("Start the Bike");
	}
	
	void stop() {
		System.out.println("Stop the Bike");
	}
}
