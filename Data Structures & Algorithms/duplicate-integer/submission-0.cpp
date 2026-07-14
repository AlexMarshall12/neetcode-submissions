class Solution {
public:
    std::set<int> tracker{};
    bool hasDuplicate(vector<int>& nums) {
        bool found_duplicate = false;
        for (auto n: nums){
            if (tracker.count(n)>0){
                return true;
            }
            tracker.insert(n);
        };
        return false;
    }
};
