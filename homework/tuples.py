# Lesson 2: Assignments | Tuples
# 1. Tuple Mastery in Python
# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument.
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
# The function should format and return a string that lists each itinerary.
# The output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def flight_itn():
    flight_info = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
    for index, flight_info in enumerate(flight_info):
        print(f'Itinerary {index + 1}: {flight_info[0]} - From {flight_info[1]} to {flight_info[2]}')
flight_itn()



# 2. Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list.
# Your task is to update this system by adding new books and ensuring no duplicates.
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.
# Existing Library Data:

library_books = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def library_system(library):
    for book, title in library_books:
        if library[0] == book:
            print("That book is already in the library!")
            return library_books
        
    library_books.append(library)
    return library_books

print(library_system(("Ulysses", "James Joyce")))
print(library_system(("The Great Gatsby", " F. Scott Fitzgerald")))
print(library_system(("Ulysses", "James Joyce")))



# 3. Mastering Tuple Packing and Unpacking in Python
# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
# Problem Statement: You are given a list of tuples, each representing a customer's order.
# Each tuple contains the customer's name, the product ordered, and the quantity.
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Susie", "Stapler", 5),
    ("Dillon", "Paper Shredder", 1)
]
for name, item, quantity in orders:
    print(f"{name} placed an order. It was for a {item} and the quantity was {quantity}.")
