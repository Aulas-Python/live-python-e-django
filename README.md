# Live de Python + Django
## Implementando um mini sistema de gerenciamento de conteúdo (Content Manager Sistem - CMS)

# Etapa por Etapa

# Etapa 1

## Construa seu ambiente de desenvolvimento

1. Isole seu ambiente usando algum virtualizador (virtualenv, pipenv, env) a seu gosto
2. Entendendo o versionamento do python e seu canivete suiço
3. Use o Sistema de instalação de pacotes do python (Python Install Packages - PIP) para instalar o que você precisa e mantenha um registro de suas dependências.
4. Ative e desative seu ambiente de desenvolvimento
5. Praticando... 

# Etapa 2

## Programando em Python

Por ser uma linguagem de programação muito rica em extensões python é usada em vários ramos de atividades. São muitas suas aplicações que vão desde infraestrutura de serviços, inteligencia artificial, bigdata pequenos e muitas cousas aplicações. Vai da criatividade!

1. Variáveis, Funções e passagem de parametros
2. Passagem de parametros usando args e kwargs
3. Orientação a objetos 
    1. Classes
    2. Construtores
    3. Métodos
    4. Instâncias
4. Modularização e Pacotes
    1. O __init__.py

# Etapa 3

## Python na Web

Nativamente python não escreve pra web, é necessário tratarmos as demandas do protocolo HTTP, neste meio de campo podemos implementar qualuqer coisa que receba as requisições (requests) do cliente (um browser por exemplo) e envie de volta as respostas (responses) desses clientes. 

Para simplificar isso, podemos usar diversas estruturas que já estão prontas, testadas, estáveis, padronizadas e de simples implementação. Estas estruturas são chamadas de Frameworks.

## Frameworks para Web 

Existem diversas soluções de frameworks para trabalhar com python na web, desde alguns bem pequenos como o microframework Flask coisas mais robustas e super completas como o Django. 

A diferença basica entre eles é que o Flask baseicamente faz o tratamento do protocolo HTTP lhe dando formas de manipular as requisições e enviar respostas, deixando o resto pra você se divertir e implementar. Já o Django ele não só faz o que o Flask faz, mas também já traz implementado um conjunto de funcionalidades como: Sessões, Autenticação de Usuário, Modelos, Templates, Banco de Dados, Internacionalização entre outras coisas.

A instalação tanto do Flask quanto do Django podem ser feitas usando o PIP.

```code
pip install django
ou
pip install flask 
```

## Dajngo The web framework for perfectionists with deadlines.

É bem explicito como o django se preocupa com produtividade, visto como um framework para pessoas exigentes com entregas, o django de fato acelera o desenvolvimento fazendo você se preocupar apenas com o que é importante para o seu projeto e deixando coisas triviais como resposabilidade do framework.

O django trabalha com Projetos e Aplicativos, então quando formos trabalhar primeiro criamos um projeto depois adcionamos aplicativos a ele. O que diferencia um projeto de um aplicativo é que o projeto é responsável por plugar os aplicativos e permitir que eles (os diversos aplicativos) falem entre si.

Um aplicativo ou aplicação é uma extrutura modularizada ou um pacote que pode e deve fazer alguma coisa. Como por exemplo, pense no projeto de um website (este é o projeto). E neste pode ter vários aplicativos. Como um aplicativo para gerenciar as páginas, um aplicativo para gerenciar os contatos do site, um aplicativo para controlar conteúdo (como um blog), um aplicativo para enquetes e por ai vai.

Quando criamos um projeto é criado um conjunto de arquivos que iremos falar sobre cada um deles.

## Mas vamos colocar a mão na massa!

# Etapa 4

## Criando um pequeno projeto

### Podemos seguir uma rotina de memorização para criarmos nossos projetos

0. Crie uma pasta para seu projeto e inicialeze um repositório git. (IMPORTANTE USAR O GIT)
```
    mkdir meuprojeto
    git init
```
1. crie seu ambiente virtual e ative
```
    python3 -m venv nomedasuaenv
    source nomedasuaenv/bin/activate
``` 

2. Instale a básico que você precisa
```
    pip install django
```
3. Construa seu projeto
```
    django-admin startproject meusite
```
4. Veja os arquivos criados pelo django
```
    tree
```
5. ... preciso sair agora ... ;) continuo depois...