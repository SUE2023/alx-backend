#!/usr/bin/env python3
"""LFUCache caching system module."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an LFU caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.frequency = {}
        self.keys_order = []

    def put(self, key, item):
        """
        Adds an item to the cache and discards
        the least frequently used item if the cache is full.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update item and frequency
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, remove the least frequently used item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used item(s)
                    min_freq = min(self.frequency.values())
                    min_freq_keys = [k for k, v in self.frequency.items()
                                     if v == min_freq]

                    # If there's a tie, use LRU (Least Recently Used)
                    if len(min_freq_keys) > 1:
                        for k in self.keys_order:
                            if k in min_freq_keys:
                                LFU_key = k
                                break
                    else:
                        LFU_key = min_freq_keys[0]

                    # Remove the LFU key from cache and order
                    del self.cache_data[LFU_key]
                    del self.frequency[LFU_key]
                    self.keys_order.remove(LFU_key)
                    print(f"DISCARD: {LFU_key}")

                # Add the new key to the cache, frequency, and order
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.keys_order.append(key)

    def get(self, key):
        """Retrieves an item by key if key is not None."""
        if key is not None and key in self.cache_data:
            # Update the frequency and reorder keys
            self.frequency[key] += 1
            self.keys_order.remove(key)
            self.keys_order.append(key)
            return self.cache_data.get(key)
        return None
