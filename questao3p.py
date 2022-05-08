import numpy as np
# sendo ele [2, 4, 6, 8, 10]
# eu pego o primeiro [2] appendo e vou subtraindo os valores consecutivos e dando append de novo
# para ficar[2,2,2,2,2]
# depois eu dou sort asc para ajudar a remover os duplicados depois
def numbers_sub(array):
    numbers = []
    numbers.append(array[0])

    for index, x in enumerate(array):
        if(not (index+1 >= len(array))):
            numbers.append(array[index+1] - array[index])

    numbers.sort()
    return numbers

# agora eu preciso recuperar os valores que estao na forma acumulativa em numbers_sub
# depois eu converto para numpy array para remover os duplicados 
# agora tem o array dos numeros que compoem a soma, eu procuro o tamanho do menor array e exibo apenas os arrays com esse tamanho
def numbers_sum(arrays_off_sum_track):
    numbers_sum = []
    for array in arrays_off_sum_track:
        numbers_sum.append((numbers_sub(array)))

    data = np.array(numbers_sum,dtype=object,)
    data = np.unique(data)
    menor = 10000000

    for d in data:
        if(len(d) < menor):
            menor = len(d)
    list = (data.tolist())

    for l in list[:]:
        if(len(l) > menor):
            list.remove(l)
    return list

# primeiro checa se existe combinacao/combinacoes que somando da n
# existindo combinacoes elas sao salvas em arrays_off_sum_track
# fica numa forma acumulativa por exemplo [2, 4, 6, 8, 10]
def sum_exists(n, p_list=[], current_sum=0, sum_track=[], arrays_off_sum_track=[]):
    if current_sum > n:
        return False
    elif current_sum == n:
        arrays_off_sum_track.append(sum_track)
        return True
    else:
        new_sums = [current_sum + x for x in p_list]
        truth_list = [sum_exists(
            n, p_list, s, sum_track+[s], arrays_off_sum_track) for s in new_sums]
        return any(truth_list)


current_sum = 0
sum_track = []
arrays_off_sum_track = []
if (sum_exists(10, [2, 3, 4], current_sum, sum_track, arrays_off_sum_track)):
    print(numbers_sum(arrays_off_sum_track))
else:
    print("não existe combinação de soma")

