package com.in28minutes.oops;

public class MotorBikeRunner {

	public static void main(String[] args) {
		
		MotorBike hyundai = new MotorBike();
		MotorBike harleys = new MotorBike();
		
		hyundai.start();
		harleys.stop();
		
		hyundai.changeSpeed(100);
		harleys.changeSpeed(90);
		
		System.out.println(hyundai.getSpeed());
		
	}

}
