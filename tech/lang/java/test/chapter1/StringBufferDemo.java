// String
public class StringBufferDemo {
    // string buffer are mutable (modification can be done)
    public static void main(String[] args) {
        StringBuffer s1 = new StringBuffer("Happy feet");
        s1.append("!!!"); // mutable
        System.out.println(s1);
    }
}