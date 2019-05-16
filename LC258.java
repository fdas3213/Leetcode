public class LC258 {
    public static int addDigits(int num){
        if (num / 10 == 0) return num;
        while (num / 10 != 0){
            int temp = 0;
            while (num != 0){
                temp += num % 10;
                num /= 10;
            }
            num = temp;
        }
        return num;
    }


    public static void main(String[] args){
        System.out.println(addDigits(38));
    }
}
