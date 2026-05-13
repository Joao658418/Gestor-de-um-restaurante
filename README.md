🍽️ Sistema de Gestão de Restaurante (V3 - Persistência JSON)

Este projeto é uma aplicação de consola robusta para a gestão integral de um restaurante. O sistema foi desenhado seguindo princípios de modularidade e persistência de dados, permitindo gerir Clientes, Pratos, Fornecedores e Funcionários com armazenamento em ficheiros locais.

📌 Índice

    Visão Geral

    Arquitetura do Sistema

    Entidades e Dados

    Códigos de Resposta (Status Codes)

    Como Executar

    Persistência de Dados

📖 Visão Geral

O sistema permite realizar todas as operações de CRUD (Create, Read, Update, Delete). A grande diferença desta versão é a integração com a biblioteca json, que garante que as informações não se perdem ao fechar o programa.
O sistema permite realizar todas as operações de CRUD (Create, Read, Update, Delete). A grande diferença desta versão é a integração com a biblioteca json, que garante que as informações não se perdem ao fechar o programa.

🏗️ Arquitetura do Sistema

O projeto está dividido em módulos independentes para facilitar a manutenção:

    main.py: O motor central. Gere os menus, recebe os inputs do utilizador e comunica com os módulos lógicos.

    clientes.py: Gestão de clientes (NIF, nome, nascimento, telefone).

    pratos.py: Gestão do cardápio (ID, preço, estrelas, ingredientes).

    fornecedores.py: Gestão de fornecedores e logística de produtos.

    funcionarios.py: Gestão de RH, salários e contratos.

    utils.py: Funções auxiliares e definições globais.

    🗂️ Entidades e Dados
    
     Entidade	Identificador Principal	  Atributos Principais
    Clientes	        NIF	              Nome, Nascimento, Telefone
    Fornecedores	    NIF      	      Morada, Telemóvel, Email, Tipo de Produto
    Funcionários	    NIF	              Cargo, Salário, Data de Entrada, Data de Saída

    🚦 Códigos de Resposta (Status Codes)

Para garantir uma comunicação clara entre as funções e a interface, utilizamos um padrão de retorno baseado em tuplos (código, objeto/mensagem):

    201 (Created): Sucesso na criação de um novo registo.

    200 (OK): Sucesso na consulta, listagem, atualização ou remoção.

    400 (Bad Request): Dados inválidos ou tentativa de duplicar registos.

    404 (Not Found): O registo solicitado não existe no ficheiro.
    
🚀 Como Executar

    Certifica-te de que tens o Python 3.x instalado.

    Mantém todos os ficheiros .py na mesma diretoria.

    Executa o comando:
    Bash

    python main.py
    500 (Internal Error): Erro inesperado no processamento de dados.

    
