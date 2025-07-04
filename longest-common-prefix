class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for x in range(1, len(strs)):
            while not strs[x].startswith(prefix):
                prefix = prefix[:-1]  # Trim last character from prefix
                if not prefix:
                    return ""  # No common prefix
        return prefix
        