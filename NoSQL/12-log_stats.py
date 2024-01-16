#!/usr/bin/env python3
"""
Function that returns the list of school having a specific topic.
"""

from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Display statistics about Nginx logs stored in MongoDB.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        None
    """
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    log_stats(logs_collection)
