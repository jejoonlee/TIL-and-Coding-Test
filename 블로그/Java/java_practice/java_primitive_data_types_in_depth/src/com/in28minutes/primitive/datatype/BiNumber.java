package com.in28minutes.primitive.datatype;

public class BiNumber {
	private int num1;
	private int num2;
	
	BiNumber (int num1, int num2) {
		this.num1 = num1;
		this.num2 = num2;
	}
	
	public int add() {
		int addNumber = this.num1 + this.num2;
		return addNumber;
	}
	
	public int multiply() {
		int multNumber = this.num1 * this.num2;
		return multNumber;
	}
	
	public void doubleValue() {
		this.num1 *= 2;
		this.num2 *= 2;
	}
	
	public int getNumber1() {
		return this.num1;
	}
	
	public int getNumber2() {
		return this.num2;
	}
}
