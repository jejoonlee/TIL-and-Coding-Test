package com.in28minutes.primitive.datatype;

import java.math.BigDecimal;

public class SimpleInterestCalculator {
	BigDecimal principal;
	BigDecimal interest;
	
	public SimpleInterestCalculator(String principal, String interest) {
		this.principal = new BigDecimal(principal);
		this.interest = new BigDecimal(interest).divide(new BigDecimal(100));
	}
	
	public BigDecimal calculateTotalValue(int year) {
		BigDecimal totalValue = principal.add(
				principal.multiply(interest
				.multiply(new BigDecimal(year))));
		return totalValue;
	}
	
}
