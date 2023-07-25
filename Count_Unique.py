def count_unique_value(list):
    unique_count = 0
    for i in range (len(list)):
        is_unique = True
        for j in range (i+1 , len(list)):
            if list[i] == list[j]:
                is_unique = False
                break
        if is_unique:
            unique_count +=1
    return unique_count

my_list = [1,2,2,3,2,11,3,2,1,4,4,4,4]
result = count_unique_value(my_list)
print(result)
