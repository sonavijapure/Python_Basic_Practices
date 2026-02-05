def left_shift(my_list):
    return  my_list[1:]+my_list[:1]

def matching_indices(l1, l2):
    # result = []
    # for i in range(len(l1)):
    #     if l1[i] == l2[i]:
    #         result.append(i)
    # return result   
    return [i for i in range(len(l1)) if l1[i] == l2[i]]

def find_middle_index(l1):
    middle_values = []
    if len(l1) % 2 == 0:
        middle_values.append(l1[round(len(l1)/2)-1])
        middle_values.append(l1[round(len(l1)/2)])
        return middle_values
    else:
        middle_values.append(l1[round(len(l1)/2)])
        return middle_values
    
def count_evens(my_list):
    # for i in my_list:
    #     if i % 2 == 0:
    #         cnt += 1
    # return cnt
    return sum(1 for i in my_list if i % 2 == 0)

def largest_number(my_list):
    large = my_list[0]
    for i in my_list:
        if i > large:
            large = i
    return large

# def largest_number(my_list):
#     return (large := i for i in my_list if i > large)

def remove_duplicates(my_list):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return result
                       
def second_largest(my_list):
    large = my_list[0]
    for i in my_list:
        if i > large and i != large:
            large = i
            for j in my_list:
                if i > j and j != large:
                    large = j
    return large


    
def second_largest1(my_list):
    largest =None #my_list[0]
    second = None

    for x in my_list:
        if x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x

    return second

def count_occurrence(my_list):
    for x in set(my_list):
        print(f"number {x} has occurred {my_list.count(x)} times.")

def split_even_odd(my_list):
    even_list = []
    odd_list = []
    for i in my_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list

def sorted_list(my_list):
    all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
    # return (False for i in range(len(my_list)-1) if my_list[i] > my_list[i+1])
    #cnt = 0
    #for i in range(len(my_list)-1):
        #if my_list[i] > my_list[i+1]: # 7>8 true 8>10 true
            #cnt += 1 # 1 2
            #if cnt == len(my_list)-1: #3 #false false
                #return True
           #return False
    #return False
    #return True



# all(iterable)
# → True if every element is truthy
# → False if any element is falsy
# Stops at the first failure.

# Think: “everything must pass”

# any(iterable)
# → True if at least one element is truthy
# → False if everything is falsy
# Stops at the first success.

# Think: “one success is enough”

# Key facts:

# Both accept lists, tuples, sets, generators

# Both short-circuit (stop early)

# They turn many conditions into one boolean

# all([]) → True

# any([]) → False

# Mental shortcut:

# all = AND

# any = OR


l1 = [2 , 3, 4, 5, 20, 100, 1]
# l2 = [1, 3, 4, 3, 1, 6]
# print(left_shift(l1))

# print(matching_indices(l1,l2))

#print(find_middle_index(l1))

# print(count_evens(l1))

# print(largest_number(l1))

# print(remove_duplicates(l1))

# count_occurrence(l1)

# print(split_even_odd(l1))

print(bool(sorted_list(l1)))
# print(len(l1))

