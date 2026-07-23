class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ''
        curr_count = 0

        stack_str = []
        stack_int = []

        for char in s:
            if char == '[':
                stack_str.append(curr_str)
                stack_int.append(curr_count)
                curr_str = ''
                curr_count = 0
            elif char == ']':
                prev_count = stack_int.pop()
                prev_str = stack_str.pop()
                curr_str = prev_str + prev_count * curr_str
            elif char.isdigit():
                curr_count = 10 * curr_count + int(char)
            else:
                curr_str += char

        return curr_str


        