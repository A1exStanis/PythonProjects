# The majority element is the element that appears more than any other element.
# You may assume that the majority element always exists in the array.
# Example 1:

# Input: nums = [3,2,3]

# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]

# Output: 2

def majority_element(nums: list) -> int:
        count_list = {}
        for i in nums:
            x = nums.count(i)
            count_list.update({x:i})
        print(count_list[max(count_list)])


majority_element([2, 2, 1, 1, 1, 2, 2])