/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
vector<Interval> Solution::merge(vector<Interval> &A) {
    
        if (A.size() <= 1) return A;
        sort(A.begin(), A.end(), [](Interval& a, Interval& b) {
            return a.start < b.start;
        });
        vector<Interval> ret;
        ret.push_back( move(A[0]) );
        for (int i=1; i<A.size(); i++) {
            if (A[i].start > ret.back().end) {       // new
                ret.push_back( move(A[i]) );
            }
            else                                             // merge
                ret.back().end = max(ret.back().end, A[i].end);
        }
        return ret;
};
