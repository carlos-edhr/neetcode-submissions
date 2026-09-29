class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        hash_map = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in hash_map:
                if not stack or stack[-1] != hash_map[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack 
        