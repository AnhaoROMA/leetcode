class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        while (start <= end)
        {
            int middle = (start + end)/2;
            if (target == nums[middle])
            {
                return middle;
            }
            if (nums[start] <= nums[middle])
            {
                if (target >= nums[start] && target < nums[middle])
                {
                    end = middle - 1;
                }
                else
                {
                    start = middle + 1;
                }
            }
            else
            {
                if (target > nums[middle] && target <= nums[end])
                {
                    start = middle + 1;
                }
                else
                {
                    end = middle - 1;
                }
            }
        }
        return -1;
    }
};