# Cantina Fatec - Sistema de Controle

## Descrição do Projeto

Este projeto foi desenvolvido para as disciplinas de Estrutura de Dados e Linguagem de Programação 2, com o objetivo de simular o funcionamento de uma cantina universitária.
O sistema permite gerenciar o estoque de produtos, registrar pagamentos, controlar vendas, gerar dados automaticamente e salvar essas informações em disco.
O principal foco do projeto foi a implementação de estruturas de dados próprias, evitando o uso direto de listas, filas e pilhas nativas do Python.

## Observação sobre o desenvolvimento

Durante o desenvolvimento deste projeto, enfrentei diversas dificuldades e precisei revisar e alterar o código várias vezes.
Isso pode ser observado pela quantidade de commits no repositório. Ao longo do processo, foi necessário corrigir erros, reorganizar estruturas e melhorar a lógica implementada.
Apesar disso, busquei aplicar o máximo do conhecimento adquirido nas disciplinas e entregar um sistema funcional, organizado e que atende aos requisitos propostos.

## Estruturas de Dados Utilizadas

Foram implementadas estruturas próprias utilizando listas encadeadas:

* Lista encadeada para controle de estoque
* Pilha para controle de pagamentos
* Fila para atendimento de clientes
* Lista encadeada para registro de vendas
* Estruturas auxiliares para itens de venda

---

## Funcionalidades

### Controle de Estoque

* Cadastro de produtos
* Controle de quantidade em estoque
* Prioridade de venda baseada na data de vencimento
* Baixa de produtos no momento da venda

### Controle de Pagamentos

* Registro de pagamentos
* Armazenamento de dados do pagador
* Controle do valor total arrecadado

### Controle de Vendas

* Simulação de compras
* Associação entre cliente, produtos e pagamento
* Registro completo de cada venda

### Geração de Dados

* Uso da biblioteca Faker
* Geração automática de pessoas, produtos e pagamentos

### Persistência de Dados

* Salvamento e carregamento com pickle
* Uso de snapshots do sistema

### Relatórios

* Relatório de vendas
* Relatório de consumo por pessoa

## Como Executar

1. Certifique-se de ter o Python instalado (versão 3.x)

2. Instale a biblioteca Faker:

```
pip install faker
```

3. Execute os arquivos conforme necessário:

Controle de estoque:

```
python controle_estoque.py
```

Controle de pagamento:

```
python controle_pagamento.py
```

Controle de venda:

```
python controle_venda.py
```

Gerador de dados:

```
python gerador_dados.py
```

Salvar dados:

```
python salvar_dados.py
```

Sistema completo com menu:

```
python cantina.py
```

## Estrutura do Projeto

* controle_estoque.py
* controle_pagamento.py
* controle_venda.py
* gerador_dados.py
* salvar_dados.py
* cantina.py


## Considerações Finais

Este projeto foi desenvolvido com foco na prática dos conceitos de estruturas de dados e organização de código.
Mesmo com as dificuldades encontradas durante o desenvolvimento, o sistema final atende aos requisitos propostos e demonstra a aplicação dos conteúdos estudados ao longo da disciplina.
