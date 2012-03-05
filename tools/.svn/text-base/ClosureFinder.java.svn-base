import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;


public class ClosureFinder {
	private Map<Long,Long> relation; 
	
	public ClosureFinder(){
		relation = new HashMap<Long, Long>();
	}
	
	public void update(long x,long y){
		Long big;
		Long small;
		if(x>y){
			big=x;
			small=y;
		}else{
			big=y;
			small=x;
		}
		
		//
		if(!relation.containsKey(big)&&!relation.containsKey(small)){
			relation.put(big, small);
			relation.put(small, small);
		}else if(!relation.containsKey(big)&&relation.containsKey(small)){
			relation.put(big, findParent(small));
		}else if(relation.containsKey(big)&&!relation.containsKey(small)){
			Long bigParent = findParent(big);
			if(bigParent>small){
				relation.put(big, small);
				relation.put(small, small);
			}else{
				relation.put(small, bigParent);
			}			
		}else if(relation.containsKey(big)&&relation.containsKey(small)){
			Long bigParent = findParent(big);
			Long smallParent = findParent(small);
			if(bigParent>smallParent){
				relation.put(big, smallParent);
			}else{
				relation.put(small, bigParent);
			}
		}
	}
	
	public Long findParent(Long x){
		Long parent = relation.get(x);
		while(parent!=x){
			return findParent(parent);
		}
		return parent;
	}
	
	public Map<Long,Set<Long>> getClusters(){
		Map<Long,Set<Long>> clusters = new HashMap<Long, Set<Long>>();
		for(Map.Entry<Long, Long> pair:relation.entrySet()){
			Long child = pair.getKey();
			Long parent= pair.getValue();
			if(clusters.containsKey(parent)){
				clusters.get(parent).add(child);
			}else{
				HashSet<Long> values = new HashSet<Long>();
				values.add(child);
				clusters.put(parent, values);
			}
		}
		return clusters;
	}
	
	public static void main(String[] args){
		ClosureFinder finder = new ClosureFinder();
		finder.update(1, 2);
		finder.update(2, 3);
		finder.update(4, 5);
		finder.update(6, 7);
		finder.update(6, 8);
		finder.update(7, 8);
		
		Map<Long,Set<Long>> clusters = finder.getClusters();
		for(Map.Entry<Long, Set<Long>> cluster:clusters.entrySet()){
			System.out.println(cluster.getKey()+"\t"+cluster.getValue().toString());
		}
	}
}
