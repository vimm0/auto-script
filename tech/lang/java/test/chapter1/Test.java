public class Test {
    Integer InstanceVariable = 19;

    public void nonStaticTest() {
        // need to create object in non-static method
        InstanceVariable = 12;
        System.out.println("Non static method");
    }

    public static void staticTest() {
        // No need to create object in static method
        System.out.println("Static method");
    }

    public static void main(String[] args) {
        Test testObject = new Test();
        System.out.println("Hello, world");
        testObject.nonStaticTest();
        staticTest();
    }
}