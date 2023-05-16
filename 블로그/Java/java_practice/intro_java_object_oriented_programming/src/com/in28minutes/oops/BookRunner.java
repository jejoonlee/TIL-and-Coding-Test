package com.in28minutes.oops;

public class BookRunner {

	public static void main(String[] args) {
		
		Book artOfComputerProgramming = new Book(100);
		Book effectiveJava = new Book(50);
		Book cleanCode = new Book(200);
		

		System.out.println(cleanCode.getCopies());

	}

}
