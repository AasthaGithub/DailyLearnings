/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public ArrayList<Interval> insert(ArrayList<Interval> list, Interval in) {

	if (list.contains(in)) {
		return list;
	}
	
	List<Interval> blist = new ArrayList<>();
    List<Interval> elist = new ArrayList<>();
	
	Interval newIn = new Interval(0, 0);
	
	for (Interval curr : list) {
		
		if (in.start > curr.start && in.end < curr.end) {
			return list;
		}
		if (in.start > curr.end) {
			blist.add(curr);
		} else if (in.end < curr.start) {
			elist.add(curr);
		} else if (in.start > curr.start && in.start < curr.end) {
			newIn.start = curr.start;
		} else if (in.end > curr.start && in.end < curr.end) {
			newIn.end = curr.end;
		}
	}
		
	if (newIn.start == 0) {
		newIn.start = in.start;
	}
	if (newIn.end == 0) {
		newIn.end = in.end;
	}
	
	blist.add(newIn);
	blist.addAll(elist);
	return (ArrayList<Interval>) blist;
	//System.out.println(blist);
    }


}