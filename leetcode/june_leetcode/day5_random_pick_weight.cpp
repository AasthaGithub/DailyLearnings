//116 ms

static const auto _____ = []()
{
    // fast IO code : this I understand
    ios::sync_with_stdio(false);
    cin.tie(0);
    return 0;
}();

/*
1.Brut Force
if our array is [1,3,4,4] and we have to return index propation to weighted
[0,1,1,1,2,2,2,2,3,3,3,3]
random function generate random number if we call 100 times random function
we assume that rand()%12 generate index from 0-11 with equal probability so whose 
arr[index] higher higher times it's index return .

2.Binary Search
if our array is [1,3,4,4] and we have to return index propation to weighted
[1,4,8,12]
  3 4  4 
random function generate random number if we call 100 times random function
we assume that rand()%12 generate index from 0-11 with equal probability so whose
*/
class Solution {
public:
    vector<int> sums;
public:
    Solution(vector<int>& w) {
        int sum = 0;
        for(int i=0;i<w.size();i++) {
            sum += w[i];
            sums.push_back(sum);
        }
    }
    
    int pickIndex() {
        int size = sums.size();
        int randomNumber = rand() % sums[size-1];
        int l=0, r=size;
        while(l<r) {
            int m = l+(r-l)/2;
            if(sums[m] <= randomNumber) l=m+1;
            else r=m;
        }
        return l;
    }
};


//112 ms fastest
class Solution {
    vector<int> mW;
    
public:
    Solution(vector<int>& w) {
        std::ios_base::sync_with_stdio(false); 
        cin.tie(nullptr); cout.tie(nullptr);
        
        mW.reserve(w.size());
        int sum = 0;
        for (auto v : w) {
            sum += v;
            mW.push_back(sum);
        }
    }
    
    int pickIndex() {
        int val = rand() % mW.back();
        
        auto it = upper_bound(mW.begin(), mW.end(), val);
        return it - mW.begin();
    }
};




//180 ms 
/*For [1,3,4,6] the probablity of choosing index 0 is 1/14, 1 is 3/14, 2 is 4/14 and 3 is 6/14.
Using Prefix sum I have converted the weight vector into a vector v:- [1,1+3, 1+3+4, 1+3+4+6].
In case of random numbers from 1 to 14, if the number is 1 then I return index 0, if number lies between [2-4] I return index 1, if number lies between [5-8] I return index 2 and if it lies in [9,14] I return index 3.
So, basically I'm returning the index of the upperbound of the random generated number from vector v.

*/

class Solution {
public:
    vector<int> v;
    Solution(vector<int>& w) {
        v.push_back(w[0]);
        for(int i=1;i<w.size();i++){
            v.push_back(v[i-1]+w[i]);
        }
    }
    
    int pickIndex() {
        int n= rand()%v[v.size()-1];
        auto it=upper_bound(v.begin(),v.end(),n);
        return it-v.begin();
    }
};
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
