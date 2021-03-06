
public class LC67 {
    public static String addBinary(String a, String b) {
        int l1 = a.length() - 1, l2 = b.length() -1;
        StringBuilder out = new StringBuilder();
        int over = 0, sum;
        while (l1 >= 0 || l2 >= 0){
            if(l1 >= 0 && l2 >= 0) sum = Character.getNumericValue(a.charAt(l1--)) + Character.getNumericValue(b.charAt(l2--)) + over;
            else if(l2 < 0) sum = Character.getNumericValue(a.charAt(l1--)) + over;
            else sum = Character.getNumericValue(b.charAt(l2--)) + over;
            out.append(sum %2);
            over = sum /2;
        }
        if (over != 0) out.append(over);
        return out.reverse().toString();
    }

    private static String Sol2(String a, String b){
        StringBuilder out = new StringBuilder();
        int l1 = a.length()-1, l2 = b.length()-1;
        int mod = 0, sum;
        while(l1 >=0 || l2 >= 0){
            if(l1 >=0 && l2 >= 0) sum = (a.charAt(l1--) - '0') + (b.charAt(l2--)-'0') + mod;
            else if (l1 < 0 && l2 >= 0) sum = b.charAt(l2--) -'0' + mod;
            else sum = a.charAt(l1--)-'0' + mod;
            mod = sum /2;
            out.append(sum%2);
        }
        if (mod !=0) out.append(mod);
        return out.reverse().toString();
    }

    public static void main(String[] args){
        System.out.println(addBinary("1010","1011"));
        System.out.println(addBinary("1","111"));
        System.out.println(addBinary("1111","1111"));
    }

}
