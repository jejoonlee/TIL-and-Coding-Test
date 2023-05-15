package com.in28minutes.oops;

public class MotorBike {
	
	// state
	private int speed;
	
	// behavior
	void changeSpeed(int speed) {
		this.speed = speed;
	}
	
	int getSpeed() {
		return this.speed;
	}
	
	void start() {
		System.out.println("Start the Bike");
	}
	
	void stop() {
		System.out.println("Stop the Bike");
	}
}
