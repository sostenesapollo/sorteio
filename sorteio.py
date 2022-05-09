import random

qnt_numbers = int(input("Quantos números você quer sortear?"))

_list_already_choosed = []
_list = list(range(qnt_numbers))

representation = ['0️⃣ ','1️⃣ ', '2️⃣ ', '3️⃣ ', '4️⃣ ', '5️⃣ ', '6️⃣ ', '7️⃣ ', '8️⃣ ', '9️⃣ ']

for i in range(qnt_numbers):
    input('Sorteando numero...')
    choosed = random.choice(_list)
    number_represented = "".join([representation[int(i)] for i in str(choosed)])
    print(f'Numero sorteado: {number_represented}')
    
    _list.remove(choosed)
    _list_already_choosed.append(choosed)

    # print(f'Números já sorteados: {_list_already_choosed}')