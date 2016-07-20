import java.util.*;
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<Integer>();
        for(int num:nums) {
            visited.add(num);
        }
        return visited.size() != nums.length;
    }
}
