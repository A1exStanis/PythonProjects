# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.

def maxArea(height: list) -> int:       ###BAD WAY
    contain_list = 0
    for i in height:
        for q in height:
            index_i = height.index(i)
            index_q = height.index(q)
            if index_i != index_q:
                contain_list = max(contain_list, (min(i, q)*abs(index_i-index_q)))
    return contain_list


def maxArea(height: list) -> int:       ###GOOD WAY
    left = 0
    right = len(height) - 1
    max_area = 0
    while right > left:
        area = (min(height[right], height[left])) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area