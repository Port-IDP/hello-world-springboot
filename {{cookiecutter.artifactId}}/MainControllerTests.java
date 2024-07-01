package com.example.helloworld.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

/**
 * Test class for the HelloWorldController.
 * This class uses the @WebMvcTest annotation to load only the web layer of the application,
 * including the controller and its dependencies.
 */
//@SpringBootTest
//@AutoConfigureMockMvc */
@WebMvcTest(MainController.class)
public class MainControllerTests {

  @Autowired
  private MockMvc mockMvc;

  @Test
  public void getHelloMessage_shouldReturnHelloWorld() throws Exception {
    mockMvc.perform(MockMvcRequestBuilders.get("/hello"))
           .andExpect(MockMvcResultMatchers.status().isOk())
           .andExpect(MockMvcResultMatchers.content().string("Hello, World!"));
  }
}
