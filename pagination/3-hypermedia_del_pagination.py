#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the database.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list containing the data for the specified page.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index_r = self.index_range(page, page_size)
        return self.dataset()[index_r[0]:index_r[1]]

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Function that return a tuple with range index
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index = (page - 1) * page_size
        end_index = page * page_size
        index_r = (start_index, end_index)
        return index_r

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''method with two integer arguments:
        index with a None default value and page_size
        with default value of 10'''
        assert index is None or (type(index) is int and 0 <= index <
                                 len(self.indexed_dataset()))
        assert type(page_size) is int and page_size > 0

        dataset_size = len(self.indexed_dataset())
        # Calculate start and end index using index_range function
        start_index = index if index is not None else 0
        end_index = start_index + page_size
        # Retrieve the dataset page based on start and end index
        data_page = []
        for i in range(start_index, min(end_index, dataset_size)):
            data_page.append(self.indexed_dataset().get(i, None))

        # Determine next index for the next page
        next_index = min(end_index, dataset_size)
        # Populate the dictionary with hypermedia information
        hyper_info = {
            "index": start_index,
            "next_index": next_index if next_index < dataset_size else None,
            "page_size": len(data_page),
            "data": [item for item in data_page if item is not None]
        }
        return hyper_info
