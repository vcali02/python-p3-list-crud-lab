#INSTRUCTION 1
def create_an_empty_list():
    return []
create_an_empty_list()




#INSTRUCTION 2
def create_a_list():
    return ["winnie", "beau", "fly", "maisy"]

create_a_list()



#INSTRUCTION 3
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

add_element_to_end_of_list(create_a_list(), "cora")



#INSTRUCTION 4
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

add_element_to_start_of_list(create_a_list(), "mason")



#INSTRUCTION 5
def remove_element_from_end_of_list(l):
    l.pop()
    return l




#INSTRUCTION 6
def remove_element_from_start_of_list(l):
    del(l[0])
    return l



#INSTRUCTION 7
def retrieve_first_element_from_list(l):
    return l[0]



#INSTRUCTION 8
def retrieve_element_from_index(l, index):
    return l[index]



#INSTRUCTION 9
def retrieve_last_element_from_list(l):
    return l[-1]

#The last element of a list is considered to be stored at an index of -1