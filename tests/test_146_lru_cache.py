from tests.conftest import import_solution

mod = import_solution("146_LRUCache")


def test_lru_basic_eviction():
    cache = mod.LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_lru_overwrite_value():
    cache = mod.LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10


def test_lru_get_missing():
    cache = mod.LRUCache(1)
    assert cache.get(42) == -1


def test_lru_recency_via_get():
    cache = mod.LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # makes 1 most-recent
    cache.put(3, 3)  # should evict 2, not 1
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3
