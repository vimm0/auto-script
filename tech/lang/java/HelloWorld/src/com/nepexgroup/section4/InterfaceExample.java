package com.nepexgroup.section4;

// interface declaration
interface Money{
    void Operation();

}
// implementation
class Debit implements Money{
    public void Operation() {
        System.out.println("Debiting the money from the account");
    }
}

class Credit implements Money{
    public void Operation(){
        System.out.println("Crediting the money to the account");
    }
}

public class InterfaceExample {
    public static void main(String[] args){
        Money c = new Credit();
        Money d = new Debit();
        c.Operation();
        d.Operation();
    }
}
