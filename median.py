def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        index_1 = int(len(sorted_list)/2 - 1)
        index_2 = int(len(sorted_list)/2)
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print (median([2,3, 5, 9]))