import re

cnpj1 = input('Digite um CNPJ: ')
#cnpj1 = '04.252.011/0001-10'
#cnpj2 = '40.688.134/0001-61'
#cnpj3 = '71.506.168/0001-11'
#cnpj4 = '12.544.992/0001-05'
REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    if eh_sequencia(cnpj):
        return False

    novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)

    if novo_cnpj == cnpj:
        print('Válido')
    else:
        print('Inválido')
    print(novo_cnpj)


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj

    else:
        return None

    total = 0

    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    if digito > 9:
        digito = 0
    else:
        digito = digito

    return f'{novo_cnpj}{digito}'


valida(cnpj1)
