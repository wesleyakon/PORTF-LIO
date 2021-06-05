casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salario?'))
ano = float(input('quantos anos deseja paga?'))
prest = casa / (ano * 12)
min = salario * 30 / 100
print('para paga uma a casa de R${} em {} Anos  !'.format(casa, ano), end =' ')
print('a prestação ficara no valor de  R${:.2f} por mês!' .format(prest))
print('seu salario com 30% é {} e valor da prestação é {:.3f}  !'.format(min, prest))
if min >= prest:
    print('finaciamneot aprovado')
else:
    print('financiamento nã aprovado ')
# programa para finacimaneto