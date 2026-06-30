class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_key = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in anagram_key:
                anagram_key[key] = []
            
            anagram_key[key].append(word)
        
        return list(anagram_key.values())




        # for i in range(len(strs)):
        #     key = "".join(sorted(strs[i]))

        #     if key not in anagram_key:
        #         anagram_key[key] = []

        #     anagram_key[key].append(strs[i])

        # return list(anagram_key.values())