import java.util.HashMap;

public class LC13 {
    public static int romanToInt(String s) {
        HashMap<Character, Integer> hm = new HashMap<>();
        hm.put('I',1);
        hm.put('V',5);
        hm.put('X',10);
        hm.put('L',50);
        hm.put('C',100);
        hm.put('D',500);
        hm.put('M',1000);

        char[] l = new char[s.length()];
        for(int i = 0;i < s.length();i++){
            l[i] = s.charAt(i);
        }
        int sum = 0;
        for(int i = 0; i< l.length-1; i++){
            if(hm.get(l[i]) < hm.get(l[i+1])) sum -= hm.get(l[i]);
            else  sum += hm.get(l[i]);
        }
        sum += hm.get(l[l.length-1]);
        return sum;
    }

    public static int betterone(String s){
        HashMap<Character, Integer> hm = new HashMap<>();
        hm.put('I',1);
        hm.put('V',5);
        hm.put('X',10);
        hm.put('L',50);
        hm.put('C', 100);
        hm.put('D', 500);
        hm.put('M', 1000);
        int out = hm.get(s.charAt(0));
        for (int i = 1; i < s.length(); i++){
            char prev = s.charAt(i-1);
            char cur = s.charAt(i);
            if (hm.get(prev) < hm.get(cur)) out -= 2*hm.get(prev);
            out += hm.get(cur);
        }
        return out;
    }

    public static void main(String[] args){
        String s1 = "IV";
        System.out.println(romanToInt(s1));
        String s2 = "III";
        System.out.println(romanToInt(s2));
        String s3 = "IX";
        System.out.println(romanToInt(s3));
        String s4 = "LVIII";
        System.out.println(romanToInt(s4));
        String s5 = "MCMXCIV";
        System.out.println(romanToInt(s5));
    }
}
