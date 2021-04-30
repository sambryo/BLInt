import re


class Interval(object):
    def __init__(self, start, end=None):
        self.start = start
        self.end = start if not end else end
        print("start: " + str(self.start) + " end: " + str(self.end))

    def parse_input(self, input_str):
        user_input = input_str.split(",")
        for s in user_input:
            pattern = re.compile(r"^[1-9]\d*-\d+$")
            dash = pattern.search(s)
            if not s.isdigit() and not dash:
                raise ValueError("Wrong input formats!")
        return user_input

    def merge(self, intervals):
        if not intervals:
            return ""
        result = set()
        try:
            val = self.parse_input(intervals)
            if len(val) == 1:
                return "".join(val)
            val.sort()
            merge_val = val[0]
            for i in range(1, len(val)):
                merge_start, merge_end, val_start, val_end = self.find_indexes(
                    merge_val, val[i])
                if merge_end < val_start:
                    result.add(merge_val)
                    merge_val = val[i]
                else:
                    merge_start = min(merge_start, val_start)
                    merge_end = max(merge_end, val_end)
                result.add(merge_val)

        except ValueError:
            print("user input format should be separated by commas and dashes for range.")
        lst_str = [str(s) for s in result]
        joined_str = ",".join(lst_str)
        return joined_str

    def find_indexes(self, merge, current_val):
        if len(merge) == 1:
            merge_start = merge_end = merge[0]
        
        merge_start, merge_end = merge[0], merge[2]

        if len(current_val) == 1:
            val_start = val_end = current_val[0]
        else:
            val_start, val_end = current_val[0], current_val[2]

        return [int(merge_start), int(merge_end), int(val_start), int(val_end)]


""" 
  The running time for this algorithms is O(nlogn). The sorting algorithm has O(nlogn)
  running time and there are O(n) operations. 
  The space complexity is O(n)
"""
