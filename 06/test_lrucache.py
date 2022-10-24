from lrucache import LRUCache

def test_cache():
    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

def test_cache2():
    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"
    cache.set("k3", "val3")
    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"

def test_cache3():
    cache = LRUCache(1)
    cache.set("k4", "val4")
    cache.set("k4", "val5")
    assert cache.get("k4") == 'val5'