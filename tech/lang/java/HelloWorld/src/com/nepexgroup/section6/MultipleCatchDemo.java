package com.nepexgroup.section6;

public class MultipleCatchDemo {
// multiple catch
    public static void main(String[] args) {
        try {
            int a = 10;
            int b = 5;
            int c = a/b;
            int d[] = {1,2,3,4};
            System.out.println(d[10]); // we are trying to access element, which is out of bounds

        }
        catch(ArithmeticException e){
            System.out.println("Arithmetic Exception has occured");
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("ArrayIndexOutOfBounds Exception has occured");

        }
        catch(Exception e){
            System.out.println("Exception has occured");

        }

        }
}
