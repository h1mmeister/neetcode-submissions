class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_count = 0

        for char in s:
            if char == '[':
                stack.append(curr_str)
                stack.append(curr_count)
                curr_count = 0
                curr_str = ''
            elif char == ']':
                prev_count = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + prev_count * curr_str
                
            elif char.isdigit():
                curr_count = 10 * curr_count + int(char)
            else:
                curr_str += char

        return curr_str


        