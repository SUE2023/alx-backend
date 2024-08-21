#!/usr/bin/env python3
"""LIFO caching system module."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents a LIFO caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Adds an item to the cache and discards
        the last item if the cache is full
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.keys_order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.keys_order.pop(3)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieves an item by key if key is not None."""
        if key is not None:
            return self.cache_data.get(key)
        return None
