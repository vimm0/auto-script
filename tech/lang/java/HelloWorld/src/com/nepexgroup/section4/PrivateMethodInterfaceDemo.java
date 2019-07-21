package com.nepexgroup.section4;
// private methods in an interface

interface Welcomes{
    default void say(){
        sayhello();
    }
    //    private(not working / run on static access modifier)
    static void sayhello(){
        System.out.println("Hello,..I'm private method.\n welcome to Nepalgunj.");
    }
}



public class PrivateMethodInterfaceDemo implements Welcomes{
    public static void main(String[] args){
        Welcomes s = new PrivateMethodInterfaceDemo();
        s.say();
    }
}
