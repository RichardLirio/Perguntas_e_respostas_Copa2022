
import os


print('BEM VINDO AO PERGUNTAS E RESPOSTAS!')
nome=str(input('Me diga seu nome desafiante:\n')).strip()
print(' Olá {0}, cada pergunta terá 4 alternativas!\nPara responder escreva somente a letra da alternetiva correspondete a sua resposta!'.format(nome.upper()))
print('Boa sorte {0}.'.format(nome.upper()))
input('Podemos começar?!')
p = 0
os.system('cls')

print('PERGUNTA NUMERO 1')
print('Qual o nome do país, que será sediada a copa do mundo de 2022?\nA)Brasil \nB)Catar \nC)Russia \nD)Espanha')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'B'): 
    pt = ( + 10)
    print('Resposta correta\nPontuação total = {0} Pontos'.format(pt))

else : print('Resposta incorreta!')

input('Podemos passar para a proxima pergunta?')
os.system('cls')


print('PERGUNTA NUMERO 2')
print('Qual é o unico país que em sua bandeira temos uma ESTRELA AMARELA?  \nA)Uruguai \nB)Suiça \nC)Camarões \nD)Senegal')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'C'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')

input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 3')
print('Qual é o primeiro nome do jogador francês Mbappe?\nA)Kylian \nB)Karim \nC)Paul \nD)Ngolo') 
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'A'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')
input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 4')
print('Qual país foi campeão da Copa do Mundo de 2014?\nA)Brasil \nB)Espanha \nC)Alemanha \nD)Holanda')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'C'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')
input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 5')
print('Qual a altura do jogador Uruguaio Edinson Cavani?\nA)2,84 \nB)1,80 \nC)1,90 \nD)1,84')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'D'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')
input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 6')
print('Qual é o peso do jogador Holandes Virgil Van Dijk ?\nA)82 kg \nB)92 kg \nC)72 kg \nD)102 kg')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'B'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')
input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 7')
print('Qual é o país do jogador Sadio Mané?\nA)Camarões \nB)Senegal \nC)Ghana \nD)Australia')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'B'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta!')
input('Podemos passar para a proxima pergunta?')
os.system('cls')


print('PERGUNTA NUMERO 8')
print('Quantos paises do Continente Africano estão participando da Copa do Mundo?\nA)2 \nB)3 \nC)4 \nD)5')
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'D'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta')
input('Podemos passar para a proxima pergunta?')
os.system('cls')


print('PERGUNTA NUMERO 9')
print('Qual jogador braseileiro nasceu em 5 de fevereiro de 1992?\nA)Casimiro \nB)Alisson \nC)Neymar \nD)Marquinhos')  
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'C'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta')
input('Podemos passar para a proxima pergunta?')
os.system('cls')

print('PERGUNTA NUMERO 10')
print('Qual jogador tem no nome a marca da cerveja mais vendida no Mexico?\nA)Hirving \nB)Guilhermo \nC)Diego \nD)Jesus Manoel')
r = str(input('Qual é a alternativa correta?\n')).upper().strip()
if (r == 'D'): 
    pt = (pt + 10)
    print('Resposta correta\nPontuação total= {0} Pontos'.format(pt))

else : print('Resposta incorreta')
input('Mostrar Pontuação final?')
os.system('cls')

input('O desafiante {0} fez no um total de {1} Pontos, Parabéns!'.format(nome.upper(),pt))
