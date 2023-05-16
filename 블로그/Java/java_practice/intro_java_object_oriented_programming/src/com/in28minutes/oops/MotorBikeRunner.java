package com.in28minutes.oops;

public class MotorBikeRunner {

	public static void main(String[] args) {
		
		MotorBike hyundai = new MotorBike(100);
		MotorBike harleys = new MotorBike(300);
		
		hyundai.start();
		harleys.stop();
		
		hyundai.changeSpeed(100);
		harleys.changeSpeed(90);
		
		System.out.println(hyundai.getSpeed());
		
		hyundai.increaseSpeed(50);
		
		System.out.println(hyundai.getSpeed());
		

		
	}

}
