class Solution:
    def decodeString(self, s: str) -> str:
        
        sub_list = []
        cur_num = 0
        result = ""

        for x in s:
            if x.isdigit():
                cur_num = cur_num * 10 + int(x)
            elif x == '[':
                sub_list.append((result, cur_num))
                cur_num = 0
                result = ""
            elif x == ']':
                prev_str, repeat = sub_list.pop()
                result = prev_str + result * repeat
            else:
                result += x
            
        return result