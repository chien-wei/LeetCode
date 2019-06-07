class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = std::lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int up = std::upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
        if (low <= up) return {low, up};
        else return {-1, -1};
    }
};