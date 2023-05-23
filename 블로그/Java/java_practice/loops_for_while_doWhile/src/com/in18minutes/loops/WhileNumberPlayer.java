package com.in18minutes.loops;

public class WhileNumberPlayer {

	private int number;
	
	WhileNumberPlayer (int num) {
		this.number = num;
	}
	
	public void printANumberTriangle() {
		int i = 1;
		
		while (i * i <= this.number) {
			System.out.print((i * i) + " ");
			i ++;
		}
		System.out.println();
	}
	
	public void printCubesUptoLimit() {
		int i = 1;
		
		while (i * i * i <= this.number) {
			System.out.print((i * i * i) + " ");
			i ++;
		}
		System.out.println();
	}
}
