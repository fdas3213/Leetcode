public class LC8 {
    public static int myAtoi(String str) {
        /* if length of string is 0, then return 0 */
        if (str.length() == 0) return 0;

        /*remove white space */
        int index = 0, sign = 1;
        long result = 0;
        while(index < str.length() && str.charAt(index) == ' '){
            index ++;
        }
        if (index == str.length()) return 0;

        /*get sign */
        if (str.charAt(index) == '+' || str.charAt(index) == '-'){
            sign = str.charAt(index) == '+' ? 1 : -1;
            index++;
        }

        /*get numbers */
        while(index < str.length()){
            if (!Character.isDigit(str.charAt(index))) break;
            int tmp = Character.getNumericValue(str.charAt(index));
            if (result > Integer.MAX_VALUE/10 || result == Integer.MAX_VALUE/10 && Integer.MAX_VALUE % 10 < tmp){
                return sign==1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            result = result * 10 + tmp;
            index++;
        }

        return sign*(int)result;
    }

    public static void main(String[] args){
        System.out.println(myAtoi("2147483648"));
        System.out.println(myAtoi("   -42"));
    }
}
