# API Blog
 
É uma `API Rest` feita em `Python` com o framework `Django` e `djangorestframework` que tem o propósito de cadastro e consulta de informações de postagens e autores de um blog.

Teste a API clickando [aqui]().
(Lembrando que a primeira requisição demora um pouco pra responder, ja que está hospedado no Heroku gratuitamente)

## Sumário
- [API Blog](#api-blog)
  - [Sumário](#sumário)
  - [Rotas](#rotas)
    - [Autores GET, POST](#autores-get-post)
    - [Publicações GET, POST](#publicações-get-post)
      - [Filtrando publicações por autores](#filtrando-publicações-por-autores)
  - [Rodando localmente](#rodando-localmente)
  - [Insomnia](#insomnia)

## Rotas 
### Autores GET, POST
```
/autores/
``` 
### Publicações GET, POST
```
/publicacoes/
``` 
#### Filtrando publicações por autores
Insira após o `serch=` o nome, sobrenome ou id do autor que deseja filtrar as postagens.
```
/publicacoes?search=Marcos
``` 

## Rodando localmente
Você deve criar um arquivo com nome `.env` contendo as informações de configurações do django e banco de dados.
Use este modelo e insira as informações à direita dos `=` sem adicionar nenhum espaço:

```
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=
NAME=
USER=
PASSWORD=
PORT=
``` 
## Insomnia

Clicke no botão abaixo para importar as configurações do insomnia para facilitar seus teste da api.

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=API_Blog&uri=https%3A%2F%2Fraw.githubusercontent.com%2FMarcosBB%2FAPI_Blog%2Fmain%2Finsomnia%2Fexport.json)