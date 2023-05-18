package com.in28minutes.ifstatement.examples;

import java.util.Scanner;

public class calenderRunner {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Is it weekday? 0 (Sunday), 6 (Saturday) : ");
		int dayNumber = scanner.nextInt();
		System.out.println(isWeekday(dayNumber));
		
		System.out.print("Input month in number : ");
		int monthNumber = scanner.nextInt();
		System.out.println(determinNameOfMonth(monthNumber));
		
		System.out.print("Input day in number : ");
		int dayNumber1 = scanner.nextInt();
		System.out.println(determinNameOfDay(dayNumber1));
	}
	
	public static boolean isWeekday(int dayNumber) {
		switch (dayNumber) {
			case 0 : return false;
			case 1 : return true;
			case 2 : return true;
			case 3 : return true;
			case 4 : return true;
			case 5 : return true;
			case 6 : return false;
		}
		return false;
	}
	
	public static String determinNameOfMonth(int monthNumber) {
		switch (monthNumber) {
			case 1 : return "January";
			case 2 : return "February";
			case 3 : return "March" ;
			case 4 : return "April";
			case 5 : return "May";
			case 6 : return "June";
			case 7 : return "July";
			case 8 : return "August";
			case 9 : return "September";
			case 10 : return "October";
			case 11 : return "November";
			case 12 : return "December";
			default : return "No such month";
		}
	}
	
	public static String determinNameOfDay(int dayNumber) {
		switch (dayNumber) {
			case 0 : return "Sunday";
			case 1 : return "Monday";
			case 2 : return "Tuesday";
			case 3 : return "Wednesday";
			case 4 : return "Thursday";
			case 5 : return "Friday";
			case 6 : return "Saturday";
			default : return "No such day";
		}
	}

}
