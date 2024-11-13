def diferenca_conjunto(list1,list2):
    return (list(set(list1)- set (list2)))
list1 = [1,2,3,4,5]
list2 = [2,4,6,7,8]
reslutado = diferenca_conjunto(list1 , list2)
print ( reslutado )