package com.springboot.jpa.service.impl;

import com.springboot.jpa.data.dao.ProductDAO;
import com.springboot.jpa.data.dto.ProductDto;
import com.springboot.jpa.data.dto.ProductReponseDto;
import com.springboot.jpa.data.entity.Product;
import com.springboot.jpa.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService {

    private final ProductDAO productDAO;

    @Override
    public ProductReponseDto getProduct(Long number) {
        Product product = productDAO.selectProduct(number);

        return ProductReponseDto.builder()
                .name(product.getName())
                .number(product.getNumber())
                .stock(product.getStock())
                .price(product.getPrice())
                .build();
    }

    @Override
    public ProductReponseDto saveProduct(ProductDto productDto) {

        Product product = Product.builder()
                .name(productDto.getName())
                .price(productDto.getPrice())
                .stock(productDto.getStock())
                .createdAt(LocalDateTime.now())
                .updatedAt(LocalDateTime.now())
                .build();

        Product savedProduct = productDAO.insertProduct(product);

        return ProductReponseDto.builder()
                .name(savedProduct.getName())
                .number(savedProduct.getNumber())
                .stock(savedProduct.getStock())
                .price(savedProduct.getPrice())
                .build();
    }

    @Override
    public ProductReponseDto changeProductName(Long number, String name) throws Exception {

        Product change = productDAO.updateProductName(number, name);

        return ProductReponseDto.builder()
                .name(change.getName())
                .number(change.getNumber())
                .stock(change.getStock())
                .price(change.getPrice())
                .build();
    }

    @Override
    public void deleteProduct(Long number) throws Exception {
        productDAO.deleteProduct(number);
    }
}
