print('*-*-*'*3,'Contagem Regressiva','*-*-*'*3,)
from time import sleep
from emoji import emojize
for c in range(10,-1,-1):
    print(c)
    sleep(1)

print(emojize(('*-*-*'*1)+':red_envelope:Feliz Ano Novo!!:red_envelope:'))
print(emojize(('*-*-*'*2)+':party_popper:Feliz Ano Novo!!:party_popper:'))
print((emojize(('*-*-*'*3)+':fireworks:Feliz Ano Novo!!:fireworks:')))
print(emojize(('*-*-*'*2)+':pine_decoration:Feliz Ano Novo!!:pine_decoration:'))
print(emojize(('*-*-*'*1)+':shooting_star:Feliz Ano Novo!!:shooting_star:'))
