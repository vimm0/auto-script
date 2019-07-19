public class ArrayDemo1 {
    public static void main(String[] args) {
        // creating array of characters
        char[] source = {'H','A','P','P','Y','L','E','A','R','N','I','N','G'};
        char[] destination  = new char[7];

        // copying elements from one array to another
        System.arraycopy(source, 0, destination, 1, 5);
        System.out.println(new String(destination));

        // deleting element from array
        int flag = 3;
        for (int i = 0; i < source.length; i++){
            // delete function
            if (flag==i){
                for (int j=i+1; i < source.length -1; j++){
                    source[i]=source[j];
                    i++;
                }
            }
        }

        System.out.println(source);
        // HAPPY
        // HAPYLEARNINGG
    }
}