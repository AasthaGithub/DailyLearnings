vector<int> Solution::maxset(vector<int> &A) {
    class Indexes {
        public:
            long maxValue;
            long startIndex;
            long size;
            Indexes(long a, long b, long c): maxValue(a), startIndex(b), size(c) {}
            bool operator>(const Indexes& second) const {
                if(maxValue == second.maxValue) /*same sum*/ {
                    if(size == second.size) {
                        return startIndex < second.startIndex ? true : false; /*first index*/
                    }
                    return size > second.size ? true : false; /*larger size*/
                }
                return maxValue > second.maxValue ? true : false; /*larger sum*/
            }
    };
    
    auto maxIndexes = Indexes(0, 0, 0);
    auto currentMax = Indexes(0, 0, 0);
    
    for(auto i = 0; i < A.size(); i++) {
        currentMax.maxValue += A[i];
        currentMax.size += 1;

        if(currentMax > maxIndexes) {
            maxIndexes = currentMax;
        }
        
        if(A[i] < 0) {
            currentMax = Indexes(0, i+1, 0);
        }
    }
    
    return std::vector<int>(A.begin() + maxIndexes.startIndex, A.begin() + maxIndexes.startIndex + maxIndexes.size);
}
