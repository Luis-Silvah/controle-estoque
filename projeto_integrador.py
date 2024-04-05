print(30*'=')
print('     Sistema de Cadastro')
print(30*'=')

cod_prd1 = input('Digite o código do produto: ')
name_prd1 = input('Digite o nome do produto: ')
dresc_prd1 = input('Adicione uma descrição ao produto: ')
ca_prd1 = float(input('Qual o custo do Produto: '))
cf = float(input('Qual os custo fixos/administrativos do comércio [%]: '))
cv = float(input('Qual a comissão de venda do produto,em porcentagem [%]: '))
iv = float(input('Qual a aliquota de imposto desejada [%]: '))
ml = float(input('Qual a margem de lucro desejada [%]: '))

print('Dados Cadastrados com sucesso!')

pv = ca_prd1/(1-((cf+cv+iv+ml)/100))
rb = pv - ca_prd1
oc = (ca_prd1)*(cf+cv+iv)/100 #ARRUMAR FORMULA
rent = rb-oc
rent_pct = rent*100/pv

cvendas = cv*pv/100
cfixo = cf*pv/100
pct_preço_venda = 100*pv/pv
pct_rb = 100*rb/pv
pct_oc = 100*oc/pv


#TERMINAR FORMATACAO TABELA
valor = 'Valor'
pct = '[%]'
print(60*'=')
print(f'Descrição {valor:^42} {pct:^12}')
print(60*'-')
print(f'Preço de Venda: {pv:^30.2f} {pct_preço_venda:^24.0f}')
print(f'Receita Bruta: {rb:^32} {pct_rb:^21}')
print(f'Custo Fixo/Administrativo: {cfixo:6} {cf:^49}')
print(f'Comissão de Vendas: {cvendas:^23} {cv:^29}')
print(f'Outros Custos: {oc:^32} {pct_oc:^20}')
print(f'Rentabilidade: {rent:^32} {rent_pct:^20}')
print(60*'=')

if rent_pct>0.1:
    if rent_pct>0.2:
        print('Lucro: Alto')
    else:
        print('Lucro: Médio')
elif rent_pct == 0:
    print('Lucro: Equilíbrio')
elif rent_pct < 0 :
    print('Lucro: Prejuízo')
else:
    print('Lucro: Baixo')
print(60*'=')