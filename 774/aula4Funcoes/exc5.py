#Crie uma função que recebe uma lista de valores e um valor a pesquisar nessa lista. Se o valor 
# está na lista devolve True se não devolve False. O programa deverá iniciar com uma lista já 
# definida e perguntar ao utilizador qual o valor a procurar nessa lista. Se o retorno da função for
# True mostra a mensagem “O valor está presente na lista”, caso contrário mostra a mensagem 
# “O valor não está presente na lista”

def pesquisa(valor,lista):
    if valor in lista:return True
    else: return False
        
lista=[]
while 0 not in lista:
    lista.append(int(input("Qual o valor(0 para terminar)--> ")));
lista.pop()#remove o 0 inserido no fim

v = int(input("Qual o valor a pesquisar? -> "))

print(lista)
if (pesquisa(v,lista)): print ("Está na lista")
else: print ("Não está!")

 
