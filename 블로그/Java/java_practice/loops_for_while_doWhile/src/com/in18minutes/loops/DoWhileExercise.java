package com.in18minutes.loops;

import java.util.Scanner;

public class DoWhileExercise {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int inputValue;
		
		do {
			System.out.print("Enter a number: ");
			inputValue = scanner.nextInt();
			if (inputValue != -1) {
				System.out.println("Cube is " + (inputValue * inputValue * inputValue));
			} else {
				System.out.println("Thank You! Have Fun!");
			}
		} while (inputValue != -1);

	}

}
