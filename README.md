# project_template #
## Sobre ##
Modelo de estrutura para projetos em fastapi framework
## Tabela de Conteúdos ##
* [Sobre](#sobre)
* [Tabela de conteúdos](#tabela-de-conteúdos)
* [Status do projeto](#status-do-projeto)
* [Recursos](#recursos)
* [Pré-requisitos](#pré-requisitos)
* [Dependências](#dependências)
* [Tecnologias](#tecnologias)
* [Testes](#testes)
* [Desenvolvimento](#desenvolvimento)
* [Deploy](#deploy)
* [API](#api)
* [Código de Conduta](#código-de-conduta)
* [Contribuindo](#contribuindo)
* [Autor](#autor)
* [Licença](#licença)
## Status do projeto ##
Em desenvolvimento
### Recursos ###
- [X] Aplicação base
- [ ] Todo
- [ ] Autenticação
### Pré-requisitos ###
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://python.org).
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
### Dependências ###
#### Utilizando Powershell ####
Criar o diretório da aplicação
```powershell
New-item -Type "Directory" <Nome do projeto/aplicação>
CD <Nome do projeto/aplicação>
```
Instalando Ambiente virtual python VirtualEnv
```powershell
python -m venv .venv --upgrade-deps
```
Habilitando o ambiente virtual python
```powershell
.venv\Script\activate
```
Instalar as dependências do projeto execute:
```powershell
.\run.cmd --install
```
Instalar as dependências de desenvolvimento do projeto execute:
```powershell
.\run.cmd --install-dev
```
Instalar as dependências de testes do projeto execute:
```powershell
.\run.cmd --install-test
```
#### Gerar Secret Key ####
Para gerar o secret key da aplicação usando python execute:
```python
import secrets
secrets.token_urlsafe(32)
```
Inserir a chave gerada no arquivo .secrets.toml

#### Extras #####
Se o powershell não estiver permissão de execução,
Para ver as permissões execute:
```powershell
Get-ExecutionPolicy -List
```
Para alterar as permissões execute o powershell no modo administrador e execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Tecnologias ###
[Dynaconf](https://www.dynaconf.com/), [FastApi](https://fastapi.tiangolo.com/), [Python](https://python.org), [PostgreSQL](https://www.postgresql.org/),[SqlAlchemy](https://www.sqlalchemy.org/)
### Testes ###
Para realizar testes, alterar a constante env do arquivo settings.toml para "testing"
#### Utilizando Powershell ####
Para realizar os testes:
```powershell
.\run.cmd --test
```
Para ver o relatório de testes em html:
Abrir no navegador o arquivo index.html da pasta htmlcov
### Desenvolvimento ###
Para rodar o programa:
```powershell
uvicorn app.main:app --reload
```
### Deploy ###

### API ###
#### Em ambiente de Desenvolvimento ###
Para listar os endpoints da aplicação, rodar a aplicação e acessar:
[API endpoints](http://127.0.0.1:8000/docs)

## Código de Conduta ##
[Código de Conduta](./code_of_conduct.md)

## Contribuindo ##
[Contribuindo](./contributing.md)

## Autor ##
[Valmir França](http://vf79.com.br)

## Licença ##
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
