public class LC43 {
    public static String multiply(String num1, String num2) {
        int l1 = num1.length(), l2 = num2.length();
        int[] products = new int[l1 + l2];
        for (int i = l1-1; i >= 0; i--){
            for (int j = l2-1; j >= 0; j--){
                int n1 = num1.charAt(i) - '0';
                int n2 = num2.charAt(j) - '0';
                products[i+j+1] += (n1*n2);
            }
        }
        int reminder = 0;
        for (int i = products.length-1; i>= 0; i--){
            int tmp = (products[i] + reminder)% 10;
            reminder = (products[i] + reminder) / 10;
            products[i] = tmp;
        }
        StringBuilder s = new StringBuilder();
        for(int num: products) s.append(num);
        while (s.length() != 0 && s.charAt(0) == '0') s.deleteCharAt(0);
        return s.length() == 0 ? "0" : s.toString();
    }

    public static void main(String[] args){
        System.out.println(multiply("123","456"));
    }
}
