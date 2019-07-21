package com.nepexgroup.section6;

// custom exception

public class CustomException extends Exception {
//    constructor overloading
    CustomException(String  s){
        super(s);
    }
    CustomException(Exception e){
        super(e);
    }
}
