

public class LC202 {
    public static boolean isHappy(int n) {
        int x = n;
        int y = n;
        while (x > 1){
            x = square(x);
            if (x == 1) return true;
            y = square(square(y));
            if (y == 1) return true;
            if (x == y) return false;
        }
        return true;
    }

    public static int square(int n){
        int out = 0;
        int copy = n;
        while (copy > 0){
            out = out + (copy%10) * (copy%10);
            copy /= 10;
        }
        return out;
    }

    public static void main(String[] args){
        System.out.println(isHappy(19));
    }
}
