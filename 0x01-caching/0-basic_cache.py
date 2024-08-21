#!/usr/bin/env python3
""" Caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic caching system."""

    def put(self, key, item):
        """Adds an item in the cache if key and item are not None."""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves an item by key if key is not None."""
        if key is not None:
            return self.cache_data.get(key)
        return None
