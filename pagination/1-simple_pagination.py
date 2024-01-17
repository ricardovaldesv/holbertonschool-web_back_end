#!/usr/bin/env python3
"""
Function named index_range that takes two integer arguments page and page_size
The function return a tuple of size two containing a start index and an
end index corresponding to the range of indexes to return in a list for those
particular pagination parameters.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

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
