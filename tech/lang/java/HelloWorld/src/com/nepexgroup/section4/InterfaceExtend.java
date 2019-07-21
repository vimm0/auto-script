package com.nepexgroup.section4;

// extend an interface with another interface
interface Walkable{
    void walk();
}

interface Runnable extends Walkable{
    void run();
}

public class InterfaceExtend implements Runnable{
    @Override
    public void walk() {
        System.out.println("Interface: Walkable");
    }

    @Override
    public void run() {
        System.out.println("Interface: Runnable");

    }
    public static void main(String[] args){
        InterfaceExtend obj = new InterfaceExtend();
        obj.walk();
        obj.run();
    }
}
