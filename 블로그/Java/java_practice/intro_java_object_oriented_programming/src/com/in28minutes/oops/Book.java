package com.in28minutes.oops;

public class Book {
	private int noOfCopies;
	
	Book (int copies) {
		this.noOfCopies = copies;
	}
	
	void setNoOfCopies(int noOfCopies) {
		if (noOfCopies >= 0) {
			this.noOfCopies = noOfCopies;
		} else {
			System.out.println("Number of copies can not be under 0");
		}
	}
	
	public int getCopies () {
		return this.noOfCopies;
	}
	
	void increaseCopies (int copies) {
		if (copies >= 0) {
			setNoOfCopies(this.noOfCopies + copies);
		} else {
			System.out.println("Input value can only be positive value");
		}
	}
	
	void decreaseCopies (int copies) {
		if (copies >= 0) {
			setNoOfCopies(this.noOfCopies - copies);
		} else {
			System.out.println("Input value can only be positive value");
		}
	}
}
