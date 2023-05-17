package com.in28minutes.primitive.datatype;

public class MyChar {
	
	private char ch = 0;
	
	MyChar (char ch) {
		this.ch = ch;
	}
	
	public boolean isvowel() {
		if (this.ch == 'a' || this.ch == 'e' || this.ch == 'i' || this.ch == 'o' || this.ch == 'u' || this.ch == 'A' || this.ch == 'E' || this.ch == 'I' || this.ch == 'O' || this.ch == 'U') {
			return true;
		}
		return false;
	}
	
	public boolean isDigit() {
		if (48 <= ch && ch <= 57) {
			return true;
		}
		return false;
	}
	
	public boolean isAlphabet() {
		if ((65 <= ch && ch <= 90) || (97 <= ch && ch <= 122)) {
			return true;
		}
		return false;
	}
	
	public boolean isConsonant() {
		if (isAlphabet() && !isvowel()) {
			return true;
		}
		return false;
	}
	
	void printLowerCaseAlphabets() {
		for (char ch = 97 ; ch <= 122 ; ch++) {
			System.out.println(ch);
		}
	}
	
	void printUpperCaseAlphabets() {
		for (char ch = 65 ; ch <= 90 ; ch++) {
			System.out.println(ch);
		}
	}
}
