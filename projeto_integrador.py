#Import Biblioteca Oracle
import oracledb

#Criacao da Conexao com o Banco de Dados
connection = oracledb.connect(
    user = 'BD150224213',
    password = 'Hhqnm9',
    dsn = '172.16.12.14/xe',
)

#Criacao da tabela no OrableDB
cursor = connection.cursor()
cursor.execute('DROP TABLE produto')

cursor.execute("""
                CREATE TABLE produto(
                nome  VARCHAR2(255) NOT NULL ,
                descricao VARCHAR2(255),
                codigo VARCHAR2(30) NOT NULL PRIMARY KEY,
                custo INTEGER NOT NULL,
                custoFixo INTEGER NOT NULL,
                comissao INTEGER NOT NULL,
                imposto INTEGER NOT NULL,
                rentabilidade NUMBER NOT NULL 
                )"""
)

#Inserts inicias na tabela
def insert_produtos():
    cursor.execute(""" 
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                VALUES ('Caneta', 'Caneta Profissional', '1', 36, 15, 5, 12, 20)
    """)

    cursor.execute(""" 
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Lapis', 'Preto B2', '2', 1, 1, 1, 1, 1)
    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'Palmeiras', '3', 10, 10, 10, 10, 50)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'São Paulo', '4', 10, 10, 10, 10, 0)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'Corinthians', '5', 10, 10, 10, 10, -20)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'Ponte Preta', '6', 10, 30, 20, 20, 29.99)
                    """)

    connection.commit()

insert_produtos()

def exibir_menu():
    print(36 * "=")
    print("Menu:")
    print(36 * "=")
    print("1. Adicionar novo produto")
    print("2. Selecionar um produto")
    print("3. Deletar do produto")
    print("4. Listar produtos")
    print("5. Sair")
    print(36 * "-")

def adicionar_produto():
    print(36 * "=")
    print("\t Sistema de Cadastro")
    print(36 * "=")

    codProduto = int(input("Digite o código do produto: "))
    nomeProduto = input("Digite o nome do produto: ")
    descProduto = input("Adicione uma descrição ao produto: ")

    custoProduto = float(input("Qual o custo do Produto: "))
    custoFixoPct = float(input("Qual os custo fixos/administrativos do comércio [%]: "))
    comissaoVendaPct = float(input("Qual a comissão de venda do produto,em porcentagem [%]: "))
    impostoVendaPct = float(input("Qual a aliquota de imposto desejada [%]: "))
    margemLucroPct = float(input("Qual a margem de lucro desejada [%]: "))

    cursor.execute(f'SELECT * FROM PRODUTO WHERE codigo = {codProduto}')

    listaProduto = []
    listaProduto.append([nomeProduto,descProduto, codProduto, custoProduto, custoFixoPct, comissaoVendaPct, impostoVendaPct, margemLucroPct])

    resultado = cursor.fetchall()

    if(len(resultado) > 0):
        print('\n Já existe um produto com esse codigo \n')
    else:
        cursor.execute(f""" 
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('{nomeProduto}', '{descProduto}', '{codProduto}', {custoProduto}, {custoFixoPct}, {comissaoVendaPct}, {impostoVendaPct}, {margemLucroPct})
                """)
        connection.commit()

        tabela_produto(listaProduto)

        print('\n Cadastro concluído com sucesso! \n')

def selecionar_produto():
    selecionaProduto = input('Digite o código do produto: ')

    cursor.execute(f'SELECT * FROM PRODUTO WHERE codigo = {selecionaProduto}')

    resultado = cursor.fetchall()
    tabela_produto(resultado)

def deletar_produto():
    codProduto = int(input('Digite o código do produto: '))

    cursor.execute(f"""
        DELETE FROM produto WHERE codigo = {codProduto}
    """)

    connection.commit()

    print("\n Produto deletado com sucesso! \n")

def listar_produto():
    cursor.execute(f'SELECT * FROM PRODUTO')

    lista = cursor.fetchall()
    for item in lista:
        tabela_produto([item])

# Campos da tabela PRODUTO

# [0] - nome 
# [1] - descricao
# [2] - codigo
# [3] - custo
# [4] - custoFixo
# [5] - comissao
# [6] - imposto
# [7] - rentabilidade

def tabela_produto(tabela):
     for row in tabela:

    # Campos
        nomeBD = row[0]
        descricaoDB = row[1]
        codigoDB = row[2]
        custoProdutoBD = row[3]
        custoFixoBD = row[4]
        comissaoVendaPctBD = row[5]
        impostoVendaPctBD =row[6]
        margemLucroPctBD = row[7]
    
    
        # Margem de lucro
        if margemLucroPctBD < 100:
            precoVenda = custoProdutoBD / (
            1 - ((custoFixoBD + comissaoVendaPctBD + impostoVendaPctBD + margemLucroPctBD) / 100)
             )
        else:
            # Preço de venda produto
            precoVenda = custoProdutoBD + ((custoFixoBD + comissaoVendaPctBD + impostoVendaPctBD + margemLucroPctBD)*custoProdutoBD / 100) 
        
        receitaBruta = precoVenda - custoProdutoBD # Receita Bruta

        comissaoVenda = comissaoVendaPctBD * precoVenda / 100 # Comissão de vendas 
        custoFixo = custoFixoBD * precoVenda / 100 # Custo fixo 
        impostoVenda = impostoVendaPctBD * precoVenda / 100 # Imposto

        outrosCustos = custoFixo + comissaoVenda + impostoVenda # Outros custos

        rentabilidade = receitaBruta - outrosCustos # Rentabilidade

        precoVendaPct = 100 * precoVenda / precoVenda # Preço de venda  %
        custoProdutoPct = custoProdutoBD * 100 / precoVenda # Custo produto %
        receitaBrutaPct = 100 * receitaBruta / precoVenda # Receita bruta  %
        outrosCustosPct = 100 * outrosCustos / precoVenda # Outros custos %

        rentabilidadePct = rentabilidade * 100 / precoVenda # Rentabilidade %

        # Tabela
        print('\n')
        print(64 * "=")

        print(f"Nome {nomeBD:^50}")

        print(f"Descrição {descricaoDB:^51}")

        print(f"Codigo {codigoDB:^51}")

        print(64 * "-")
        print(f"Descrição {'Valor':^51} {'[%]':^2}")
        print(64 * "-")
        print(f"Preço de Venda: {precoVenda:^40.2f} {precoVendaPct:7.0f}") 
        print(f"Custo de Aquisição (Fornecedor): {custoProdutoBD:^2.2f} {custoProdutoPct:^48.0f}")
        print(f"Receita Bruta: {receitaBruta:^42.2f} {receitaBrutaPct:^11.0f}") 
        print(f"Custo Fixo/Administrativo: {custoFixo:11.2f} {custoFixoBD:^48.0f}") 
        print(f"Comissão de Vendas: {comissaoVenda:^31.2f} {comissaoVendaPctBD:^24.0f}") 
        print(f"Imposto: {impostoVenda:^53.2f}{impostoVendaPctBD:.0f}") 
        print(f"Outros Custos: {outrosCustos:^42.2f} {outrosCustosPct:^10.0f}") 
        print(f"Rentabilidade: {rentabilidade:^42.2f} {rentabilidadePct:^10.0f}") 
        print(64 * "=")


        if margemLucroPctBD > 20:
            print("Lucro: Alto")
        elif margemLucroPctBD > 10:
            print('Lucro Médio')    
        elif margemLucroPctBD > 0:
            print("Lucro: Baixo")
        elif margemLucroPctBD < 0:
            print("Lucro: Prejuízo")
        else:
            print("Lucro: Equilíbrio")
        print(64 * "=")
        print('\n')

while True:
    exibir_menu()
        
    opcao = input("Escolha uma opção: ")
        
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        selecionar_produto()
    elif opcao == "3":
        deletar_produto()
    elif opcao == "4":
        listar_produto()
    elif opcao == "5":
        break
    else:
        print("\n Opção inválida. Tente novamente. \n ")