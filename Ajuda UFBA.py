valid_n = False

while valid_n == False:
    n1 = input('digite a nota da 1 avaliação: ')
    try:
        n1 = float(n1)
        if n1 < 0 or n1 > 10:
            print ('o numero precisa estar entre ZERO e DEZ')
        else:
            valid_n = True
    except:
        print ('formato invalido, digite apenas numerais e substitua virgulas por pontos')
        
valid_f = False
while valid_f == False:
    f = input('digite o total de faltas: ')
    try:
        f = float(f)
        if f < 0 :
            print ('as faltas devem estar ser maiores que 0')
        else:
            valid_f = True
    except:
        print ('formato inválido, letras e virgulas não são aceitos')
        
p = 8 - f
n2 = (50 - (n1*4))/6
if p >= 0:
    print (' Precisará tirar: {} para passar'.format (n2))
    print (' poderá faltar: ', p,'aulas')
else:
    print(' SE FODEU OTÁRIO, perdeu por falta')
    
fim = input(' Pressione ENTER para terminar') 
