package com.in28minutes.firstjavaproject;

public class MultiplicationTable {
	
	void printMultiply(int number, int from, int to) {
		for (int i = from; i <= to ; i ++) {
			System.out.printf("%d * %d = %d", number, i, number * i).println();
		}
	}
}

