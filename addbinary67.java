import java.lang.Math;

public class addbinary67 {
    public static void main(String[] args){
        System.out.println(addBinary("10","11"));
        System.out.println(addBinary("110","10"));
        System.out.println(addBinary("1010","1011"));

    }

    public static String addBinarySolution(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() -1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';
            if (i >= 0) sum += a.charAt(i--) - '0';
            sb.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }


    public static String addBinary(String a, String b) {
        StringBuilder out = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, reminder = 0;
        int sum = 0;
        while (i >= 0 || j >= 0){
            if (i < 0) sum = Character.getNumericValue(b.charAt(j--));
            else if (j < 0) sum = Character.getNumericValue(a.charAt(i--));
            else sum = Character.getNumericValue(a.charAt(i--)) + Character.getNumericValue(b.charAt(j--));
            out.append((sum + reminder) % 2);
            reminder = (sum + reminder) / 2;
        }
        if (reminder != 0) out.append(reminder);
        return out.reverse().toString();
    }
}
