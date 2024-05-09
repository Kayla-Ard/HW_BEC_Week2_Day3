# Lesson 3: Assignments | Sets
# 1. Python Sets Adventure
# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:
    # Destinations that both airlines fly to.
    # Destinations unique to your airline.
    # Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print(f"The destinations that both airline fly to are: {common_destinations}.")

our_exclusive_routes = our_routes.difference(competitor_routes)
print(f"The destinations exclusive to our routes are: {our_exclusive_routes}.")

unique_destinations = our_routes.symmetric_difference(competitor_routes)
print(f"The destinations that neither airline share are: {unique_destinations}")



# 2. Set Operations in Data Analysis
# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated.
# Write a Python script to remove duplicates and display the unique customer IDs.
# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
remove_duplicates = set(customer_ids)
customer_ids = list(remove_duplicates)
print(customer_ids)
