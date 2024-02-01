from time import sleep
import requests
import pyautogui
from random import randint



def linhatam(msg):
    print('-' *len(msg))
    print(f'{msg}')
    print('-' *len(msg))
    

def linha():
    print('')
    
    
pessoas = []
cont_pessoa = pessoa_velha = pessoa_nova = mulher_mais30 = homem_mais30 = 0
nome_pessoa_velha = nome_pessoa_nova = ''

produtos = []
cont_produto = prod_caro = prod_barato = prod_mais5k = prod_mais1k = 0
nome_prod_caro = nome_prod_barato = ''
total = 0

cont_request = 0
cont_auto = 0
cont_rand = 0
url_linkedin = 'https://platform.linkedin.com/litms/allowlist/voyager-web-feed'
headers_linkedin = {
                        ':authority': 'platform.linkedin.com',
                        ':method': 'GET',
                        ':path': '/litms/allowlist/voyager-web-feed',
                        ':scheme': 'https',
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'dnt': '1',
                        'if-none-match': 'e86ad4c0f4bd6fdc82d6ddb91916d142',
                        'origin': 'https://www.linkedin.com',
                        'referer': 'https://www.linkedin.com/',
                        'sec-ch-ua': '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Linux"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.0.0',
}
sair = False
while not sair:
    print('[1] Cadastrar pessoas\n'
          '[2] Cadastrar produtos\n'
          '[3] Request-linkedin\n'
          '[4] pesquisar preço do dolar\n'
          '[5] Numero aleatorio\n'
          '[6] Sair\n')
    opc = int(input('Digite sua opção:'))
    if opc == 1:
        while True:
            continuar = ' '
            sexo = ' '
            linhatam('Cadastro de pessoas:'.center(100))
            nome = str(input('Digite o nome:'))
            idade = int(input('Digite a idade:'))
            while sexo not in 'MF':
                sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0]
                if sexo in 'MF':
                    cadastro_pessoas = {'Nome':nome, 'Idade':idade, 'Sexo':sexo}
                    pessoas.append(cadastro_pessoas)
                    cont_pessoa += 1
                    print('Pessoa adicionada com sucesso!')
            
            if cont_pessoa == 1 or idade > pessoa_velha:
                nome_pessoa_velha = nome
                pessoa_velha = idade
            
            elif cont_pessoa == 1 or idade < pessoa_nova:
                nome_pessoa_nova = nome
                pessoa_nova = idade
                
            elif idade > 30 and sexo == 'F':
                mulher_mais30 += 1
            
            elif idade > 30 and sexo == 'M':
                homem_mais30 += 1    
                        
            while continuar not in 'SN':
                continuar = str(input('Quer continuar [S/N]:')).upper().strip()[0]
            if continuar == 'N':
                break
    elif opc == 2:
        while True:
            continuar2 = ' '
            linhatam('Cadastro de produtos:'.center(100))
            produto = str(input('Digite o produto:'))
            preco = float(input('Digite o preço R$'))
            cadastro_produtos = {'Produto':produto, 'Preço':preco}  
            produtos.append(cadastro_produtos)
            total += preco
            cont_produto += 1
            print('Produto cadastrado com sucesso')
            
            if cont_produto == 1 or preco > prod_caro:
                nome_prod_caro = produto
                prod_caro = preco
            
            elif cont_produto == 1 or preco < prod_barato:
                nome_prod_barato = produto
                prod_barato = preco
                
            elif preco > 5000:
                prod_mais5k += 1
            
            elif preco > 1000:
                prod_mais1k += 1            
            
            while continuar2 not in 'SN':
                continuar2 = str(input('Quer continuar [S/N]:')).upper().strip()[0]
            if continuar2 == 'N':
                break
    
    elif opc == 3:
        while True:
            continuar3 = ' '
            linhatam('Request-linkedin'.center(100))
            try:
                print('-'*149)
                r = requests.get(url_linkedin, params=headers_linkedin)
                print(r.text)
                linha()
                print(f'status:{r.status_code}')
                cont_request += 1
                print('-'*149)
            except:
                print('erro de conexão')   
            while continuar3 not in 'SN':
                continuar3 = str(input('Quer continuar [S/N]:')).upper().strip()[0]
            if continuar3 == 'N':
                break     
    
    elif opc == 4:
        while True:
            continuar4 = ' '
            linhatam('Pesquisar preço do dolar:'.center(100))    
            pyautogui.press('win')
            sleep(1) 
            pyautogui.write('google')
            sleep(1)
            pyautogui.press('enter')
            sleep(3)
            pyautogui.write('valor do dollar')
            sleep(1)
            pyautogui.press('enter')
            cont_auto += 1
            while continuar4 not in 'SN':
                continuar4 = str(input('Quer continuar [S/N]:')).upper().strip()
            if continuar4 == 'N':
                break
    elif opc == 5:
        while True:
            continuar5 = ' '
            linhatam('Numero aleatório'.center(100))
            rand = randint(0, 100)
            cont_rand += 1
            print(f'seu numero aleatório é:{rand}')
            while continuar5 not in 'SN':
                continuar5 = str(input('Quer continuar [S/N]:')).upper().strip()[0]  
            if continuar5 == 'N':
                break          
    elif opc == 6:
        sair = True         

linhatam('Sua lista de pessoas é:')
for item in pessoas:
    print(item)
linha() 
print(f'você cadastrou {cont_pessoa} pessoas no sistema') 
print(f'a pessoa mais velha foi {nome_pessoa_velha} e tem {pessoa_velha} anos de idade')
print(f'a pessoa mais nova foi {nome_pessoa_nova} e tem {pessoa_nova} anos de idade')    
print(f'foram {mulher_mais30} mulheres com mais de 30 anos')
print(f'foram {homem_mais30} homens com mais de 30 anos')         
linha()
linhatam('Sua lista de produtos é:')
for item in produtos:
    print(item) 
linha()
print(f'você cadastrou {cont_produto} produtos no sistema')
print(f'o total da compra deu R${total:.2f}')
print(f'o produto mais caro foi {nome_prod_caro} e custou R${prod_caro:.2f}')
print(f'o produto mais barato foi {nome_prod_barato} e custou R${prod_barato:.2f}')
print(f'foram {prod_mais5k} produtos mais de R$5000')
print(f'foram {prod_mais1k} produtos mais de R$1000')   
linha()
print(f'você realizou {cont_request} Request no linkedin')
linha()
print(f'você realizou {cont_auto} vezes a pesquisa do dollar')
print(f'você gerou {cont_rand} numeros aleatório')
sleep(1)
linhatam('Obrigado volte sempre, finalizando programa.'.center(100))
sleep(1)
