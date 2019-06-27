from dataclasses import dataclass
from typing import List
from functools import reduce


class mixed_rad_num():
    def __init__(self, bases: List[int]):
        self.bases = bases
        self.value = 0

    def add_one(self):
        self.value += 1

    def calc_mynum_mixed_radix_form(self) -> List[int]:
        mixed_format = []
        val_for_calc = self.value
        for num in self.bases[::-1]:
            mixed_format.insert(0, val_for_calc % num)
            val_for_calc = val_for_calc // num
        #print(mixed_format)
        return mixed_format


def str_manip(num: int, my_char: str) -> str:
    if num == 0:
        return my_char
    elif num == 1:
        return my_char.capitalize()
    elif num == 2:
        return '0'
    else:
        return '-'


def string_maker(passw: str, values: List[int]) -> str:
    return_str = ""
    for m_char, val in zip(passw, values):
        return_str += str(str_manip(val, m_char))
    return return_str


my_passw = "asd_od"
my_bases = [2, 2, 2, 1, 3, 2]
assert (len(my_bases) == len(my_passw))
result = 1
maximum = reduce(lambda x, y: x * y, my_bases)
my_num = mixed_rad_num(my_bases)
result_list = []

for _ in range(maximum):
    template_val = my_num.calc_mynum_mixed_radix_form()
    #print(string_maker(my_passw, template_val))
    result_list.append(string_maker(my_passw, template_val))
    my_num.add_one()
assert (len(result_list) == len(set(result_list)))
print(result_list)
