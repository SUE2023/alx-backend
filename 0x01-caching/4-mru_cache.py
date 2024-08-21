#!/usr/bin/env python3
"""MRU caching system module."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents a MRUCache caching system."""
    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Adds an item to the cache and discards
        the least recently used item if the cache is full
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key to update its position later
                self.keys_order.remove(key)
            else:
                # If the cache is full, remove the least recently used item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    MRU_key = self.keys_order.pop(3)
                    del self.cache_data[MRU_key]
                    print(f"DISCARD: {MRU_key}")

            # Add the key to the end of the order list
            self.keys_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key if key is not None and updates its order."""
        if key is not None and key in self.cache_data:
            # Update key's position in order list to mark it as recently used
            self.keys_order.remove(key)
            self.keys_order.append(key)
            return self.cache_data.get(key)
        return None
