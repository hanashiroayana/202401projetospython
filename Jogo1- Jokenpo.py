import random
import emoji
from time import sleep

print('*'*5,'JOKENPÔ!','*'*5)
print('*'*5,'INICIAR','*'*5)
print('Escolha sua arma! Eu já escolhi a minha...')

while True:
    pc = random.randint(1,3)
    if pc == 1:
        pc_emoji = emoji.emojize('PAPEL! :raised_hand:')
    elif pc == 2:
        pc_emoji = emoji.emojize('PEDRA! :raised_fist:')
    else:
        pc_emoji = emoji.emojize('TESOURA! :victory_hand:')

    escolha = int(input(emoji.emojize('Digite 1 para PAPEL:raised_hand: \nDigite 2 para PEDRA:raised_fist:\nDigite 3 para TESOURA:victory_hand:\n')))
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PÔ!')
    sleep(0.5)

    print(f'Eu escolhi:{pc_emoji}')

    if pc == escolha:
        print('EMPATE! Vamos mais uma vez?\n')
    else:
        if (pc == 1 and escolha == 3) or (pc == 2 and escolha == 1) or (pc == 3 and escolha == 2):
            print (emoji.emojize('VOCÊ GANHOU!:face_screaming_in_fear: '))
        elif (pc==1 and escolha == 2) or (pc == 2 and escolha == 3) or (pc == 3 and escolha == 1):
            print(emoji.emojize('EU GANHEI HAHAHAHA. Revanche? :smirking_face:'))
        else:
            print(emoji.emojize('Número inválido. Nem sabe brincar direito... :nauseated_face:'))

