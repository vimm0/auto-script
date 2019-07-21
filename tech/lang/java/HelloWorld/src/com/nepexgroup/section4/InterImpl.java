package com.nepexgroup.section4;

//static method in an interface
interface Inter1{
    int a = 10;
    static void dispaly(){
        System.out.println("Static method in Interface");
    }
}
public class InterImpl implements Inter1 {
    public static void main (String[] args){
        Inter1.dispaly();
    }
}
