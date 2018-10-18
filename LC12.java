public class LC12 {
    public static String intToRoman(int num) {
        if (num == 0) return null;
        int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] maps = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        String out = "";

        for (int i = 0; i < values.length; i++){
            while(num >= values[i]){
                out += maps[i];
                num -= values[i];
            }
        }
        return out;
    }

    public static void main(String[] args){
        int t1 = 17;
        System.out.println(intToRoman(17));
    }
}
