#!/usr/bin/env python3
"""
Function that changes all topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Args:
        mongo_collection: pymongo collection object.
        name (str): The school name to update.
        topics (list): List of strings representing the list of
            topics approached in the school.
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)


if __name__ == "__main__":
    from pymongo import MongoClient
