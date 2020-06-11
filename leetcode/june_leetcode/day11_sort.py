#16 ms
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        p1 = 0
        curr = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p1], nums[curr] = nums[curr], nums[p1]
                p1 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
                
                
#cpp
class Solution {
public:
    void sort012(vector<int>&a) { 
    int n=a.size();
    int lo = 0; 
    int hi = n- 1; 
    int mid = 0; 
    while (mid <= hi) { 
        switch (a[mid]) { 
        case 0: 
            swap(a[lo++], a[mid++]); 
            break;
        case 1: 
            mid++; 
            break; 
        case 2: 
            swap(a[mid], a[hi--]); 
            break; 
            } 
        } 
    } 
    void sortColors(vector<int>& nums) {
        sort012(nums);
    }
};
