print(30*'=')
print('     Sistema de Cadastro')
print(30*'=')

cod_prd1 = input('Digite o código do produto: ')
name_prd1 = input('Digite o nome do produto: ')
dresc_prd1 = input('Adicione uma descrição ao produto: ')
ca_prd1 = float(input('Qual o custo do Produto: '))
cf = float(input('Qual os custo fixos/administrativos do comércio: '))
cv = float(input('Qual a comissão de venda do produto,em porcentagem: '))
iv = float(input('Qual a aliquota de imposto desejada: '))
ml = float(input('Qual a margem de lucro desejada: '))

pv = ca_prd1/(1-((cf+cv+iv+ml)/100))
rb = pv - ca_prd1
oc = (ca_prd1)*(cf+cv+iv)/100
rent = rb-oc
rent_pct = rent*100/pv
print(f'Preço de Venda: {pv}')
print(f'Receita Bruta: {rb}')
print(f'Outros Custos: {oc}')
print(f'Rentabilidade: {rent}')


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
