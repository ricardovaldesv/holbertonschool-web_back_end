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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Retrieve a specific page of data from a CSV file.
        '''
        assert type(page) is int and type(page_size) is int, "Must be int"
        assert page > 0 and page_size > 0, "The page and page_size must be > 0"
        list_of_data = []
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            indexes = index_range(page, page_size)
            for num, line in enumerate(reader):
                if num in range(indexes[0], indexes[1]):
                    list_of_data.append(line)
        return list_of_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''method that takes the same arguments (and defaults)as get_page
        and returns a dictionary containing the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        '''
        dict_of_data = {}
        indexes = index_range(page, page_size)
        if (indexes[0] + 1) > len(self.dataset()):
            dict_of_data["page_size"] = 0
        else:
            dict_of_data["page_size"] = indexes[1] - indexes[0]
        dict_of_data["page"] = page
        dict_of_data["data"] = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        dict_of_data["next_page"] = page + 1 if page < total_pages else None
        dict_of_data["prev_page"] = page - 1 if page > 1 else None
        dict_of_data["total_pages"] = total_pages
        return dict_of_data


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return tuple([start_index, end_index])
