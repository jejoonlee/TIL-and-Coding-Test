package com.springboot.jpa.service;

import com.springboot.jpa.data.dto.ProductDto;
import com.springboot.jpa.data.dto.ProductReponseDto;


public interface ProductService {
    ProductReponseDto getProduct(Long number);

    ProductReponseDto saveProduct(ProductDto productDto);

    ProductReponseDto changeProductName(Long number, String name) throws Exception;

    void deleteProduct(Long number) throws Exception;
}
