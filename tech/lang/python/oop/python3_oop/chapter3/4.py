class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
# >>> longkeys = LongNameDict()
# >>> longkeys['hello'] = 1
# >>> longkeys['longest yet'] = 5
# >>> longkeys['hello2'] = 'world'
# >>> longkeys.longest_key()
# 'longest yet'
