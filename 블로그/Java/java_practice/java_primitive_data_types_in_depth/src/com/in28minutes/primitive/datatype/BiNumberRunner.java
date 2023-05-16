package com.in28minutes.primitive.datatype;

public class BiNumberRunner {

	public static void main(String[] args) {
		
		BiNumber numbers = new BiNumber(2, 3);
		System.out.println(numbers.add());
		System.out.println(numbers.multiply());
		numbers.doubleValue();
		System.out.println(numbers.getNumber1());
		System.out.println(numbers.getNumber2());
	}

}
