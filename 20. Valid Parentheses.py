class Solution(object):
    def isValid(self, s):
        dictionary = dict(('()', '[]', '{}'))
        stack = []
        for index in s:
            if index in '([{':
                stack.append(index)
            elif len(stack) == 0 or index != dictionary[stack.pop()]:
                return False
        return len(stack) == 0