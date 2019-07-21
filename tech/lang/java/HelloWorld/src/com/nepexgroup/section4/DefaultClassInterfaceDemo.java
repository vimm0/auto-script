package com.nepexgroup.section4;
// Default methods in an interface

interface Welcome{
    // default method
    default void say(){
        System.out.println("Hello, welcome to Nepalgunj");
    }
    // abstract method
    void hello(String msg);
}

public class DefaultClassInterfaceDemo implements Welcome{
    public void hello(String msg){
        // implementation of abstract method
        System.out.println(msg);
    }
    public static void main(String[] args){
        DefaultClassInterfaceDemo out = new DefaultClassInterfaceDemo();
        out.say(); // default method
        out.hello("Happy Learning"); // calling abstract method
    }
}
