package com.example.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * This is the main class of the application.
 * It is annotated with @SpringBootApplication which is a convenience annotation
 * that adds all the required annotations for a Spring Boot application.
 */
@SpringBootApplication
public class MainApplication {

  public static void main(String[] args) {
    SpringApplication.run(MainApplication.class, args);
  }

}
