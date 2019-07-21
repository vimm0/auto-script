package com.nepexgroup.section4;
// class extending one class and implementing more than one interface
interface Walk{
    void walk();
}

interface Run{
    void run();
}

class Animal implements Walk, Run {
    public void walk() {
        System.out.println("Walkable interface is getting executed");
    }
    public void run(){
        System.out.println("Runnable interface is getting executed");

    }
}

class Human extends Animal{

}

public class OneClassMultipleImplement {
 public static void main(String[] args){
     Walk h1 = new Human();
     Run h2= new Human();
     h1.walk();
     h2.run();
 }
}