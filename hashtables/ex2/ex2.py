#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __repr__(self):
        return f"source: {self.source}, destination: {self.destination}"

"""
- Create a trip using the Ticket class 
source --> starting airport
destination --> next airport

- Return an array of strings with the ENTIRE route of your trip 
- We need to *link* tickets together to reconstruct the trip --(SJC BOS) vs (BOS JFK)
- Hash each ticket - w starting is key and destination is value
-
"""

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    print('length', length)
    for t in tickets:
        #t is each ticket object
        print('t:', t)

        #insert each ticket into the hash table based on key
        hash_table_insert(hashtable, t.source, t.destination)

    start = "NONE"
    #loop through every item in hash table
    for i in range(length):
        #set the route equal to retrieval of hash table
        route[i] = hash_table_retrieve(hashtable,start)
        #set start equal to the route[0] route[1]
        start = route[i]
    return route[:len(route)-1] #1 gets rid of None


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")


tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8,ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))

#  ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP", "SLC", "PIT", "ORD"]