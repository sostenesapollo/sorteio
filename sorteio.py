import random

min_value = int(input("Qual o intervalo de números para sortear? \nDe:"))
max_value = int(input("Até:"))

qnt_chooses = int(input("Quantos números você quer sortear?\n"))

_list_already_choosed = []
_list = list(range(min_value, max_value+1))

representation = ['0️⃣ ','1️⃣ ', '2️⃣ ', '3️⃣ ', '4️⃣ ', '5️⃣ ', '6️⃣ ', '7️⃣ ', '8️⃣ ', '9️⃣ ']

for i in range(qnt_chooses):
    input('Sorteando numero...')
    choosed = random.choice(_list)
    number_represented = "".join([representation[int(i)] for i in str(choosed)])
    print(f'Numero sorteado: {number_represented}')
    
    _list.remove(choosed)
    _list_already_choosed.append(choosed)

    # print(f'Números já sorteados: {_list_already_choosed}')