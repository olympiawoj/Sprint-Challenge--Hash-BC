#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):

    print('weights', weights)
    print('length', length)
    print('limit', limit)

    #instantiate an instance of Hashtable class
    ht = HashTable(16)


    """
    YOUR CODE HERE

    Goal = find two items whose SUM of weights EQUAL the LIMIT weight 
    weight[i] + weight[i] = LIMIT
    Alternatively, LIMIT - weight[i] = another weight[i]
    Return --> a TUPLE ()
    Loop through every item in the hash table using the length 
    """

    if length < 2:
        return None

    for i in range(length):
  
        print('i:', i, ', weights[i]:', weights[i])

        #retrieve takes the hash table and key & for every index, finds value correspending to key
        #limit - weight[i] = another weight[i] or a key! 
        #value will return none if key is not found, otherwise retrieves the value stored with the key 
        val = hash_table_retrieve(ht, (limit - weights[i]))
        print('val', val)
                


        #populate the hash table, storing the value w/ the given key 
        hash_table_insert(ht, weights[i], i)

        #i and val are indices of two weights that equal the limit
        if val is not None:
            # The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index. 
            if i > val:
                return [i, val]
            else:
                return [val, i]


   


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
print(get_indices_of_item_weights(weights, length, limit))


# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

weights_2 = [4, 4]
answer2 = get_indices_of_item_weights(weights_2, 2, 8)
print('answer2', answer2)   #[1, 0]


#    def test_ex1_2(self):
#         weights_2 = [4, 4]
#         answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
#         self.assertTrue(answer_2[0] == 1)
#         self.assertTrue(answer_2[1] == 0)