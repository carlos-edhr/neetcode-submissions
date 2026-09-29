class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1) , len(s2)
        if m > n:
            return False
        
        
        target = [0] * 26
        window = [0] * 26

        for ch in s1:
            target[ord(ch) - ord('a') ] += 1
        
        matches = sum(1 for i in range(26) if target[i] == 0)

        for right, ch in enumerate(s2):
            idx = ord(ch) - ord("a")
            window[idx] += 1
            if window[idx] == target[idx]:
                matches += 1
            elif window[idx] == target[idx] + 1:
                matches -= 1
            
            if right >= m:
                left_idx = ord(s2[right - m]) - ord("a")
                window[left_idx] -= 1
                if window[left_idx] == target[left_idx]:
                    matches += 1
                elif window[left_idx] == target[left_idx] - 1:
                    matches -= 1
            
            if matches == 26:
                return True
                
        return False
