package com.springboot.jpa.data.dto;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class ChangeProductNameDto {
    private Long number;
    private String name;
}
