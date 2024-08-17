#!/usr/bin/env python3
""" Pagintion index parameters"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Paginate the dataset."""

    # Calculate the starting and ending indices
    start_index = (page - 1) * page_size
    end_index = page * page_size

    # Slice the dataset
    return (start_index, end_index)
