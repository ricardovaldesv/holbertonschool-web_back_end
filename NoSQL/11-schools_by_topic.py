#!/usr/bin/env python3
"""
Function that returns the list of school having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search.

    Returns:
        A list containing school documents with the specified topic.
    """
    query = {"topics": {"$in": [topic]}}
    schools = list(mongo_collection.find(query))
    return schools


if __name__ == "__main__":
    from pymongo import MongoClient
