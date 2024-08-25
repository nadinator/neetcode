def topKFrequent(nums:list[int], k:int)->list[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)] # index is the frequency, item in inner list is the number(s)
		# Last item in freq is the list of numbers in nums with the highest frequency count
        
		# Get the frequency of each number
        for v in nums:
            count[v] = 1 + count.get(v, 0)
		# Save that frequency as key and the number as value
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
		# Iterate backwards through freq to get k-frequent
        for i in range(len(freq)-1, 0, -1):
            if freq[i]:
                result.extend(freq[i])
                if len(result) == k:
                    return result