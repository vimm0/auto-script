public class ArrayDemo {
    public static void main(String[] args) {
        int[] arrayOfIntegers = new int[] { 1, 2 };// single dimensional arrary declaration and initialization
        int[] array = { 2, 4, 6, 8 };
        int[][] multiDimensionalArray = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
        System.out.println(array[0]);
        System.out.println(array[1]);
        // System.out.println(array[5]); // ArrayIndexOutOfBoundsException
        System.out.println(arrayOfIntegers[0]);
        System.out.println(multiDimensionalArray[1].length);
    }
}