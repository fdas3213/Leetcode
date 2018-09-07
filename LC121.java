
public class LC121 {
    public static int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int min_prices = prices[0];
        int max_profit = 0;
        for (int i = 1; i<prices.length;i++){
            if (prices[i] < min_prices) min_prices = prices[i];
            if (max_profit <(prices[i] - min_prices)) max_profit = prices[i]-min_prices;
        }
        return max_profit;

    }

    public static void main(String[] args){
        int[] t1 = {7,1,5,3,6,4};
        int[] t2 = {7,6,4,3,1};
        int[] t3  = {2,4,1};
        System.out.println(maxProfit(t1));
        System.out.println(maxProfit(t2));
        System.out.println(maxProfit(t3));
    }
}
