package com.nepexgroup.section3;

// Encapsulation

class Employee1 {
    private String name;
//    getters
    public String getName(){
        return name;
    }
//    setters (is not good practice)
    public void setName(String name){
        this.name = name;
    }
}



public class DemoEncaps {
    public static void main(String[] args){
        Employee1 e = new Employee1();
        e.setName("Alex");
        System.out.println(e.getName());
    }
}
