package com.springboot.jpa.controller;

import com.springboot.jpa.data.dto.ChangeProductNameDto;
import com.springboot.jpa.data.dto.ProductDto;
import com.springboot.jpa.data.dto.ProductReponseDto;
import com.springboot.jpa.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/product")
@RequiredArgsConstructor
public class ProductController {

    private final ProductService productService;

    @GetMapping()
    public ResponseEntity<ProductReponseDto> getProduct(Long number) {
        ProductReponseDto productReponseDto = productService.getProduct(number);

        return ResponseEntity.status(HttpStatus.OK).body(productReponseDto);
    }

    @PostMapping()
    public ResponseEntity<ProductReponseDto> createProduct(@RequestBody ProductDto productDto) {
        ProductReponseDto productReponseDto = productService.saveProduct(productDto);

        return ResponseEntity.status(HttpStatus.OK).body(productReponseDto);
    }

    @PutMapping()
    public ResponseEntity<ProductReponseDto> getProduct(
            @RequestBody ChangeProductNameDto changeProductNameDto
    ) throws Exception {
        ProductReponseDto productReponseDto = productService.changeProductName(
                changeProductNameDto.getNumber(),
                changeProductNameDto.getName()
        );

        return ResponseEntity.status(HttpStatus.OK).body(productReponseDto);
    }

    @DeleteMapping()
    public ResponseEntity<String> deleteProduct(Long number) throws Exception {
        productService.deleteProduct(number);

        return ResponseEntity.status(HttpStatus.OK).body("정상적으로 삭제되었습니다");
    }

}