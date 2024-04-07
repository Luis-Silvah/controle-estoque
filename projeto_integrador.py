print(36 * "=")
print("\t Sistema de Cadastro")
print(36 * "=")

codProduto = input("Digite o código do produto: ")
nomeProduto = input("Digite o nome do produto: ")
descProduto = input("Adicione uma descrição ao produto: ")

custoProduto = float(input("Qual o custo do Produto: "))
custoFixoPct = float(input("Qual os custo fixos/administrativos do comércio [%]: "))
comissaoVendaPct = float(input("Qual a comissão de venda do produto,em porcentagem [%]: "))
impostoVendaPct = float(input("Qual a aliquota de imposto desejada [%]: "))
margemLucroPct = float(input("Qual a margem de lucro desejada [%]: "))

print("Dados Cadastrados com sucesso!")

# Preço de venda produto
precoVenda = custoProduto / (
    1 - ((custoFixoPct + comissaoVendaPct + impostoVendaPct + margemLucroPct) / 100)
)

receitaBruta = precoVenda - custoProduto # Receita Bruta

comissaoVenda = comissaoVendaPct * precoVenda / 100 # Comissão de vendas 
custoFixo = custoFixoPct * precoVenda / 100 # Custo fixo 
impostoVenda = impostoVendaPct * precoVenda / 100 # Imposto

outrosCustos = custoFixo + comissaoVenda + impostoVenda # Outros custos

rentabilidade = receitaBruta - outrosCustos # Rentabilidade

precoVendaPct = 100 * precoVenda / precoVenda # Preço de venda  %
custoProdutoPct = custoProduto * 100 / precoVenda # Custo produto %
receitaBrutaPct = 100 * receitaBruta / precoVenda # Receita bruta  %
outrosCustosPct = 100 * outrosCustos / precoVenda # Outros custos %

rentabilidadePct = rentabilidade * 100 / precoVenda # Rentabilidade %

# Tabela
print(64 * "=")
print(f"Descrição {"Valor":^51} {"[%]":^2}")
print(64 * "-")
print(f"Preço de Venda: {precoVenda:^40.2f} {precoVendaPct:7.0f}") 
print(f"Custo de Aquisição (Fornecedor): {custoProduto:^2.2f} {custoProdutoPct:^48.0f}")
print(f"Receita Bruta: {receitaBruta:^42.2f} {receitaBrutaPct:^11.0f}") 
print(f"Custo Fixo/Administrativo: {custoFixo:11.2f} {custoFixoPct:^48.0f}") 
print(f"Comissão de Vendas: {comissaoVenda:^31.2f} {comissaoVendaPct:^24.0f}") 
print(f"Imposto: {impostoVenda:^53.2f}{impostoVendaPct:.0f}") 
print(f"Outros Custos: {outrosCustos:^42.2f} {outrosCustosPct:^10.0f}") 
print(f"Rentabilidade: {rentabilidade:^42.2f} {rentabilidadePct:^10.0f}") 
print(64 * "=")

if rentabilidadePct > 10:
    if rentabilidadePct > 20:
        print("Lucro: Alto")
    else:
        print("Lucro: Médio")
elif rentabilidadePct == 0:
    print("Lucro: Equilíbrio")
elif rentabilidadePct < 0:
    print("Lucro: Prejuízo")
else:
    print("Lucro: Baixo")
print(64 * "=")
