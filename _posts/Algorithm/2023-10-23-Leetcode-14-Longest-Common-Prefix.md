# Longest Common Prefix in Python


```
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        # Return an empty string if the input list is empty.
        # 배열이 비어있을 경우 빈 스트링을 리턴
        if not strs:
            return ""
        
        # Sort the strings to easily determine the shortest and longest ones.
        # 가장 긴 스트링과 가장 짧은 스트링을 쉽게 찾기위해 문자열 배열을 정렬
        strs.sort()

        # Assign the first (shortest) and last (longest) strings from the sorted list.
        # 가장 긴 문자열, 긴 문자열을 쉽게 사용하기 위해 선언
        first = strs[0]
        last = strs[-1]

        i = 0

        # Compare characters between the shortest and longest strings. If these strings have a common prefix, 
        # 가장 짧은 문자열과 가장 짧은 문자열이 서로 동일하면 strs는 이미 정렬이 됐기 때문에 모든 값이 동일하다고 인식
        # it ensures all other strings in the list also share that prefix up to the length of the shortest string.
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
```