import typing
import collections

from numpy import arange

def quick_select(nums: typing.List[int], idx: int, left: int, right: int):
    if left == right:
        return nums[left]

    def partition(nums, left, right):
        p, pivot = left,nums[right]
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p+=1
        nums[p], nums[right] = nums[right], nums[p]
        return p

    p = partition(nums, left,right)
    if p > idx:
        return quick_select(nums, idx, left, p-1)
    elif p < idx:
        return quick_select(nums, idx, p+1, right)
    else:
        return nums[p]


def topKFrequent(nums: typing.List[int], k: int):
    freq = collections.Counter(nums)
    unique = list(freq.keys())
    
    def quick_select(left, right, unique, k):
        if left == right:
            return unique[left:]
        
        def partition(left, right, unique):
            p, pivot = left, freq[unique[right]]
            for i in range(left,right):
                if freq[unique[i]] <= pivot:
                    unique[i], unique[p] = unique[p], unique[i]
                    p+=1
            
            unique[p], unique[right] = unique[right], unique[p]
            return p
        
        p = partition(left, right, unique)
        if p > k:
            return quick_select(left, p-1, unique, k)
        elif p < k:
            return quick_select(p+1, right, unique, k)

        return unique[p:]
    
    return quick_select(0, len(unique)-1,unique, len(unique)-k)


def merge(arr1: typing.List[int], arr2: typing.List[int]) -> typing.List[int]:
    result = []
    i, j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    
    if i < len(arr1):
        result.extend(arr1[i:len(arr1)])
    
    if j < len(arr2):
        result.extend(arr2[j:len(arr2)])
    
    return result


def mergeK_sorted_arrays(arrays: typing.List[typing.List[int]]) -> typing.List[int]:
    if not arrays:
        return []
    
    elif len(arrays) == 1:
        return arrays[0]

    middle = len(arrays)//2
    left = mergeK_sorted_arrays(arrays[:middle])
    right = mergeK_sorted_arrays(arrays[middle:])

    return merge(left,right)

