package com.nepexgroup.section6;

public class ExceptionDemo {
    public static void main(String[] args) {

    int a = 9;
    int b = 0;
    try {
        System.out.println(a/b);
    }
    catch(Exception e){
        System.out.println("We cannot divide any number by zero. Divide by Zero Exception has occured");
        }

    }
}
