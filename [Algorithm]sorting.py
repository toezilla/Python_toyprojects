from typing import List

class Sort:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-16
    Purpose: Implementation of Sorting Algorithms
    """
    
    def __init__(self, array: List):
        self.array = array

    def selection_sort(self) -> List:
        array = self.array
        for i in range(length := len(array)):
            min_index = -1
            for j in range(i, length):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        print("SelectionSort completed!")
        return array

    def bubble_sort(self) -> List:
        array = self.array
        for i in range(length := len(array)):
            for j in range(i, length-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("BubbleSort completed!")
        return array

    def insertion_sort(self) -> List:
        array = self.array
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
                    break
        print("InsertionSort completed!")
        return array

    def merge_sort(self, array: List) -> List:
        if (length := len(array)) < 2:
            return array

        mid = length // 2
        array_one = self.merge_sort(array[:mid])
        array_two = self.merge_sort(array[mid:])

        merged_array = []
        index_one, index_two = 0, 0
        while index_one < len(array_one) and index_two < len(array_two):
            if array_one[index_one] < array_two[index_two]:
                merged_array.append(array_one[index_one])
                index_one += 1
            else:
                merged_array.append(array_two[index_two])
                index_two += 1
        merged_array += array_one[index_one:]
        merged_array += array_two[index_two:]

        return merged_array

    def quick_sort(self, array: List) -> List:
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        lesser_array, equal_array, greater_array = [], [], []
        for num in array:
            if num < pivot:
                lesser_array.append(num)
            elif num > pivot:
                greater_array.append(num)
            else:
                equal_array.append(num)
        return self.quick_sort(lesser_array) + equal_array + self.quick_sort(greater_array)