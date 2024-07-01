package com.example.helloworld.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello world controller class.
 * This class is annotated with @RestController, which is a convenience annotation
 * that combines @Controller and @ResponseBody. This annotation tells Spring to
 * render the response as plain text, and not as a view.
 */
@RestController
public class HelloWorldController {
  
  /**
   * this method returns hello world message.
   *
   * @return hello world message
   */
  @GetMapping("/hello")
  public String getHelloMessage() {
    return "Hello, World!";
  }
}
