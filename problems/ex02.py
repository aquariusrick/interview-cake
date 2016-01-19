"""
Write a function get_products_of_all_ints_except_at_index() that takes
a list of integers and returns a list of the products.

For example, given:
  [1, 7, 3, 4]

your function would return:
  [84, 12, 28, 21]

by calculating:
  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""


def get_product_of_all_ints_except_at_index(nums):
    result_list = [nums[1], nums[0]]
    last_num = nums[1]
    for n in nums[2:]:
        new_value = result_list[-1] * last_num
        for i in range(len(result_list)):
            result_list[i] *= n

        result_list.append(new_value)
        last_num = n

    return result_list
