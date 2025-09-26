class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};


/* 
Time Complexity:  O(N*N), Because we are traversing the whole array again and again for every integer.
Space Complexity: O(1), Since, we are not using any extra space. */
