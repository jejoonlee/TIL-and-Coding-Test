package com.springboot.jpa.data.dto;


import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class ProductReponseDto {
    private Long number;
    private String name;
    private int price;
    private int stock;
}
