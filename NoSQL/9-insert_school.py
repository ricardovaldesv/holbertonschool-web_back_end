#!/usr/bin/env python3
"""
Function that inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the
            fields of the new document.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    from pymongo import MongoClient
