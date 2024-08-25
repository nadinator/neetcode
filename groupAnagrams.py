from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list) # string counts -> list of strings

        for s in strs:
            count = [0] * 26 # 26 characters in the alphabet
            for c in s:
                # Set up counts for each character in the string
                count[ord(c) - ord("a")] += 1
            # `count` of anagrams is the same
            ans[tuple(count)].append(s) # Must use tuple cuz immutable keys only
            
        return ans.values() # Values are the lists of strings