def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if atual - ano < 18 and atual - ano > 2016:
        print(f'Com {idade} anos o voto é OPCIONAL.')
    elif atual - ano >= 65:
        print(f'Com {idade} anos o voto é OPCIONAL.')
    elif atual - ano < 16:
        print(f'Com {idade} anos NÃO VOTA.')
    else:
        print(f'Com {idade} anos o voto é OBRIGATÓRIO.')

#programa principal
ano = int(input('Em que ano a pessoa nasceu? '))
voto(ano)


'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if atual - ano < 18 and atual - ano > 2016:
        return (f'Com {idade} anos o voto é OPCIONAL.')
    elif atual - ano >= 65:
        return (f'Com {idade} anos o voto é OPCIONAL.')
    elif atual - ano < 16:
       return (f'Com {idade} anos NÃO VOTA.')
    else:
        return (f'Com {idade} anos o voto é OBRIGATÓRIO.')

#programa principal
print(voto(2000))'''
