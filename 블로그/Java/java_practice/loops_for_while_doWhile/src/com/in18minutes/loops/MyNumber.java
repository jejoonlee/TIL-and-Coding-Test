package com.in18minutes.loops;

public class MyNumber {
	private int number;
	
	MyNumber (int num) {
		this.number = num;
	}
	
	public boolean isPrime() {
		for (int i = 2; i <= (this.number + 1) / 2; i++) {
			if (this.number % i == 0) {
				return false;
			}
		}
		return true;
	}
	
	public int sumUptoN() {
		int ans = 0;
		
		for (int i = 1; i <= this.number; i ++) {
			ans += i;
		}
		
		return ans;
	}
	
	public int sumOfDivisors() {
		int answer = 0;
		for (int i = 2; i <= (this.number + 1) / 2; i ++) {
			if (this.number % i == 0) {
				
				if (i == this.number/i) {
					answer += i;
				} else {
					answer += (i + (this.number / i));
				}
			}
		}
		return answer;
	}
	
	public void printANumberTriangle() {
		for (int i = 1; i <= this.number; i ++) {
			for (int j = 1 ; j <= i ; j ++) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
	}
	
}
