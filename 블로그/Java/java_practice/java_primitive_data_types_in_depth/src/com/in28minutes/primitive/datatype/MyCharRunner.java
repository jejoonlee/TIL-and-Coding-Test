package com.in28minutes.primitive.datatype;

public class MyCharRunner {

	public static void main(String[] args) {
		
		MyChar myChar = new MyChar('z');
		
		System.out.println(myChar.isvowel());
		System.out.println(myChar.isDigit());
		System.out.println(myChar.isAlphabet());
		System.out.println(myChar.isConsonant());
		myChar.printLowerCaseAlphabets();
		myChar.printUpperCaseAlphabets();

	}

}
