#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list containing all documents in the collection.
        Returns an empty list if no documents are present.
    """
    documents = list(mongo_collection.find())
    return documents


if __name__ == "__main__":
    from pymongo import MongoClient
