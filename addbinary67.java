import java.lang.Math;

public class addbinary67 {
    public static void main(String[] args){
        //System.out.println(addBinary("10","11"));
        System.out.println(addBinary("110","10"));
    }

    public static String addBinary(String a, String b) {
        if (a.length() == 0) return b;
        if (b.length() == 0) return a;
        int i = a.length() - 1;
        int j = b.length() - 1;
        String out = "";

        while (i >= 0 && j >= 0){
            int sum = Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(j));
            if (sum == 2){
                out += "0";
                out += "1";
            }else out += Integer.toString(sum);
            i --;
            j --;

        }

        if (a.length() > b.length()){
            out += a.substring(0,i);
        }else if (b.length() > a.length()) out += b.substring(0,j);

        return out;
    }
}
