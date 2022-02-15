import random
from datetime import datetime
import copy

def create_random_array(size):
    array=list(range(0, size))
    random.shuffle(array)
    return array
    
def create_best_array(size):
    array=list(range(0, size))
    return array
    
def create_worst_array(size):
    array=[]
    while size>0:
        array.append(size-1)
        size-=1
    return array

def bubble_sort(array, size):
    start_time=datetime.now()
    compare_counter=0
    swap_counter=0
    
    for i in range (size-1):
        for j in range (size-i-1):
            compare_counter+=1
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
                swap_counter+=1

    sorting_time=datetime.now()-start_time

    print("\n      Бульбашкою: ")
    #print(array)
    print("         Кількість порівнянь: "+str(compare_counter))
    print("         Кількість перестановок: "+str(swap_counter))
    print("         Час сортування: "+str(sorting_time))

def comb_sort(array2, size):
    start_time=datetime.now()
    swap_counter=0
    compare_counter=0

    swaps = True
    step=size
    while step > 1 or swaps:
        step = max(1, int(step / 1.247))
        swaps = False
        for i in range(size - step):
            compare_counter+=1
            if array2[i] > array2[i+step]:
                array2[i], array2[i+step] = array2[i+step], array2[i]
                swap_counter+=1
                swaps = True

    sorting_time=datetime.now()-start_time

    print("\n      Гребінцем: ")
    #print(array2)
    print("         Кількість порівнянь: "+str(compare_counter))
    print("         Кількість перестановок: "+str(swap_counter))
    print("         Час сортування: "+str(sorting_time))



size=int(input("Введіть розмір масиву: "))
array=create_random_array(size)
array2=copy.deepcopy(array)
print("\nВипадкова послідовність: ")
#print(array)
bubble_sort(array, size)
comb_sort(array2, size)

array=create_best_array(size)
array2=copy.deepcopy(array)
print("\nУпорядкована послідовність: ")
#print(array)
bubble_sort(array, size)
comb_sort(array2, size)

array=create_worst_array(size)
array2=copy.deepcopy(array)
print("\nЗворотньо упорядкована послідовність: ")
#print(array)
bubble_sort(array, size)
comb_sort(array2, size)
