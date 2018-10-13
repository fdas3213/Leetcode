import java.util.ArrayList;
import java.util.List;

public class LC119 {
    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> out = new ArrayList<>();
        out.add(1);
        if (rowIndex == 0) return out;
        for (int i = 1; i <= rowIndex; i++){
            ArrayList<Integer> tmp = new ArrayList<>();
            tmp.add(1);
            for(int j = 1; j<i;j++){
                tmp.add(out.get(j) + out.get(j-1));
            }
            tmp.add(1);
            out = tmp;
        }
        return out;
    }
}
