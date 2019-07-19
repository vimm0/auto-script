// Demo-calculator
public class Calculator {
    // method overloading: mulitple methods with the same name and return type,
    // but different number of arguments or arguments of different data types
    public Integer add(Integer arg1, Integer arg2) {
        arg1 = 100; // does not reflect at all 
        Integer result = arg1 + arg2;
        return result;
    }
    public Integer add(Integer arg1, Integer arg2, Integer arg3){
        Integer result = arg1 + arg2 + arg3;
        return result;
    }
    public static void main(String[] args) {
        Calculator calcualtorObject = new Calculator();
        int arg1 = 10;
        int arg2 = 20;
        int arg3 = 30;
        System.out.println("arg1 before is " + arg1);
        Integer result = calcualtorObject.add(arg1, arg2); // call by value
        System.out.println("arg1 after is " + arg1);
        System.out.println("Result of addition is " + result);
        Integer resultFromNewMethod = calcualtorObject.add(arg1, arg2, arg3); // call by value
        System.out.println("Result of addition is " + resultFromNewMethod);

    }
}