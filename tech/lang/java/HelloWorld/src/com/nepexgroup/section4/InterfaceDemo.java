package com.nepexgroup.section4;

// Interface

interface Shape {
    //    all its methods is by default abstract or add abstract (no problem)
    abstract float area();
}



public class InterfaceDemo {
    public static void main(String[] args){
    }
}

// circle class implements shape
class Circle implements Shape{
    public float area(){
        return 1.2f;
    }
}