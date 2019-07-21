package com.nepexgroup.section6;

public class ThrowDemo1 {
    public static int divide(int a, int b) throws Exception{
        int c;
        c = a/b;
        return c;
    }
    public static void main(String[] args) {
      try{
          ThrowDemo t = new ThrowDemo();
          int ans = divide(10, 0);
          System.out.println("Result is: "+ ans);
      }
      catch(Exception e){
          System.out.println("Exception is: "+ e);
      }
    }
}
