package com.nepexgroup.section6;
// nested try blocks
public class NestedTryDemo {
    public static void main(String[] args) {
        try{
            try{
                int a = 50;
                int b = 0;
                System.out.println("Division is: "+ (a/b));

            }
            catch(ArithmeticException e) {
                System.out.println("Arithmetic exception (Divide by zero) has occured");
            }
        }
        catch(Exception e){
            System.out.println("Exception has occured");
        }
    }
}
