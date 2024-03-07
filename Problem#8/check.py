def in_order(nums):
    # Type your code here.
    ordered = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            ordered = False
            break
    return ordered
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
