# github-api-user-activty

Este projeto implementa um pequeno utilitário em Python para buscar a atividade recente de um usuário do GitHub e exibir informações relevantes no terminal.

## Estrutura do projeto

- `main.py` - ponto de entrada do projeto.
- `app/services/api_service.py` - serviço responsável por fazer chamadas à API do GitHub e formatar os eventos retornados.
- `app/routers/` - pasta reservada para futuras rotas ou componentes de CLI, se expandir o projeto.

## Como funciona atualmente

Atualmente, o projeto roda principalmente por meio de `app/services/api_service.py`, que consome a API pública do GitHub para obter eventos de usuário e formata mensagens sobre ações como push, issues e stars.

## Objetivo

O objetivo deste projeto é praticar:
- consumo de APIs REST;
- manipulação de JSON;
- desenvolvimento de um utilitário simples em Python;
- trabalho com dados da API do GitHub.

## Projeto proposto

Este projeto segue a proposta do roadmap.sh para praticar a manipulação de dados com a API do GitHub:

https://roadmap.sh/projects/github-user-activity
