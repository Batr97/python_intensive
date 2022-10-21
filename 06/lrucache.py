class LRUCache:

    def __init__(self, lim):
        self.lim = lim
        self.cache = {}
        self.lru = {}
        self.tlru = 0

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.lru[key] = self.tlru
            self.tlru += 1
            return self.cache[key]

    def argmin(self, dictionary):
        if not dictionary:
            return None
        min_val = min(dictionary.values())
        return [k for k in dictionary if dictionary[k] == min_val][0]

    def set(self, key, val):
        if len(self.cache) < self.lim:
            self.cache[key] = val
            self.lru[key] = self.tlru
            self.tlru += 1
        else:
            key_min = self.argmin(self.lru)
            self.cache.pop(key_min)
            self.lru.pop(key_min)
            self.cache[key] = val
            self.lru[key] = self.tlru
            self.tlru += 1
