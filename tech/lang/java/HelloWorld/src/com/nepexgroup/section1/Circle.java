package com.nepexgroup.section1;

public class Circle extends Shape{
//    we have to implement area abstract method
//    if we dont want to extend and  abstract class like circle
    @Override
    long area() {
//        overriding method
        return (long) 1.23;
    }
}
