import oracledb

connection = oracledb.connect(
    user = 'BD150224213',
    password = 'Hhqnm9',
    dsn = '172.16.12.14/xe',
)


cursor = connection.cursor()
cursor.execute(''' 
                CREATE TABLE produto(
                nome  VARCHAR2(255) NOT NULL ,
                descricao VARCHAR2(255),
                codigo VARCHAR2(30) NOT NULL PRIMARY KEY,
                custo INTEGER NOT NULL,
                custoFixo INTEGER NOT NULL,
                comissao INTEGER NOT NULL check (comissao > 0),
                imposto INTEGER NOT NULL,
                rentabilidade INTEGER NOT NULL 
                )
''')

#INSERT DE DADOS
cursor.execute('''
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Caneta', 'Caneta Profissional', '1', 36, 15, 5, 12, 20);
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Lapis', 'Preto B2', '2', 1, 1, 1, 1, 1);
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Caderno', 'Palmeiras', '3', 10, 10, 10, 10, 50);
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Caderno', 'Sao Paulo', '4', 10, 10, 10, 10, 0);
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Caderno', 'Corinthians', '5', 10, 10, 10, 10, -20);
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade)
                VALUES ('Caderno', 'Ponte Preta', '6', 10, 30, 20, 20, 29.99);
               ''')
connection.commit()
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
if margemLucroPct < 100:
    precoVenda = custoProduto / (
        1 - ((custoFixoPct + comissaoVendaPct + impostoVendaPct + margemLucroPct) / 100)
    )
else:
    precoVenda = custoProduto + ((custoFixoPct + comissaoVendaPct + impostoVendaPct + margemLucroPct)*custoProduto / 100) 
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
print(f"Descrição {'Valor':^51} {'[%]':^2}")
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


if margemLucroPct > 20:
    print("Lucro: Alto")
elif margemLucroPct > 10:
    print('Lucro Médio')    
elif margemLucroPct > 0:
    print("Lucro: Baixo")
elif margemLucroPct < 0:
    print("Lucro: Prejuízo")
else:
    print("Lucro: Equilíbrio")
print(64 * "=")
