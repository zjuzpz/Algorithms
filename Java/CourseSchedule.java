import java.util.*;
public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> lookup = new HashMap<Integer, Set<Integer>>();
        for(int i = 0; i < prerequisites.length; i++) {
            if(!lookup.containsKey(prerequisites[i][0])) {
                lookup.put(prerequisites[i][0], new HashSet<Integer>());
            }
            lookup.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
        Set<Integer> learnt = new HashSet<Integer>();
        Set<Integer> visited = new HashSet<Integer>();
        for(Integer key: lookup.keySet()) {
            visited.add(key);
            if(!DFS(learnt, lookup, key, visited)) {
                return false;
            }
            visited.remove(key);
            learnt.add(key);
        }
        return true;
    }
    
    public boolean DFS(Set<Integer> learnt, Map<Integer, Set<Integer>> lookup, int key, Set<Integer> visited) {
        for(Integer i: lookup.get(key)) {
            if(visited.contains(i)) {return false;}
            if(!learnt.contains(i) && lookup.containsKey(i)) {
                visited.add(i);
                if(!DFS(learnt, lookup, i, visited)) {return false;}
                visited.remove(i);
                learnt.add(i);
            }
        }
        return true;
    }
    
	public static void main(String[] args) {
		int[][] prerequisites = {
				{1, 2}
		};
		System.out.println(new CourseSchedule().canFinish(2, prerequisites));
	}

}
