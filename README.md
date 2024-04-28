# :ledger: Projeto Integrador

## Campos do Banco de dados

### Tabela Produtos

-    nome 
-    descricao
-    codigo
-    custo
-    custoFixo
-    comissao
-    imposto
-    rentabilidade

## Configuração docker

Criação do container
````js
    docker-compose up --build --no-recreate -d
````

Atualizar o docker-compose
````js
    docker-compose up -d
````

Acessar o terminal para iniciar projeto
````js
    docker exec -it projeto_integrador sh
````

# Python

Instalar a dependências:
```python
   pip install oracledb
```

Rodar arquivo por linha de comando
```python
    python projeto_integrador.py
```
