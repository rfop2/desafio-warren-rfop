# Calcula o reverso de n
def checkReversible (n):
     
    rev = 0
   
    # Flag para saber qnd parar
    flag = n
     
    while (flag != 0):
        rem = flag % 10
        rev *= 10
        rev += rem
        flag //= 10
     
    # Calcula a soma do numero
    # com o seu reverso
    sum = rev + n
   
    # Verifica se o numero reverso
    # tem numeros impares
    while (sum and ((rem % 2) != 0)):
        rem = sum % 10
        sum //= 10
     
    if (sum == 0):
        print(n)
# exibe os numeros reversos de 1 a 1 milhao
for x in range(1,1000001):
    checkReversible(x)
