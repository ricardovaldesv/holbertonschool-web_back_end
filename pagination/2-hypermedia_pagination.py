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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:

            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page (equivalent to return from previous task)
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset
              as an integer
        """
        list_data = self.get_page(page, page_size)
        dic = {}
        if page >= int(len(self.dataset())) / page_size:
            dic['page_size'] = 0
        else:
            dic['page_size'] = page_size
        dic['page'] = page
        dic['data'] = list_data
        if page == int(len(self.dataset())) / page_size:
            dic['next_page'] = None
        else:
            dic['next_page'] = page + 1

        if page == 0 or page == 1:
            dic['prev_page'] = None
        else:
            dic['prev_page'] = page - 1

        dic['total_pages'] = int(len(self.dataset()) / page_size)
        return dic
