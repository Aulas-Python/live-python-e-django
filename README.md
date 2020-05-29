# Live de Python + Django
## Implementando um mini sistema de gerenciamento de conteúdo (Content Management System - CMS)

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
    cd meuprojeto
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
    django-admin startproject meusite .
```
4. Veja os arquivos criados pelo django
```
    tree
```
5. Para executar o projeto. 
```
    python3 manage.py runserver
```
6. Abra em um navegador de internet indo até o endereço, http://localhost:8000


## O MVC do Django ou melhor MTV

Quando desenvolvemos alguma cosia, geralmente nos deparamos com coisas rotineiras, determinadas estruturas já foram implementadas anteriormente por outras pessoas. Isso quer dizer que coisas se repetem, algumas coisas se repetem tanto que acabam sendo padronizadas e isso é muito bom, porque acaba diminuindo nosso gasto de energia com determinados problemas.

Uma forma interessante para echergarmos essas repetições de padrões é olharmos para as fachadas de casas em uma cidade, perceba que elas acabam se repetindo em forma, modelos, estruturas.

> __Arquitetura__ refere-se a toda construção e modelagem artificial do ambiente físico, incluindo seu processo de projeto e o produto deste, sendo a palavra também usada para definir os estilos e métodos de projeto das construções de uma época.  (Wikipedia)

Agora pensando no mesmo conceito de arquitetura sobe a ótica do desenvolvimento de software, quais são:

0. o fisico é o abstrato (software)
1. os processos?
2. o produto?
3. o que é o estilo?

## Tudo são padrões!

Um padrão comum no desenvolvimento de produtos para web é separar a aplicação em no mínimo 3 paters denominada de camadas. No padrão de 3 Camadas separamos em: Modelo de dados, Visualização, Controle. Este modelo é conhecido como Arquitetura MVC (Model - View - Control). O Framework

### O Modelo (Model)

É a forma como vemos os dados de uma aplicação. São classe a quel eplicitamos todas as caracteristicas de um determinado objeto da aplicação.

### A Visualiazação (View) - No django são chamadas de Template (T)

O que nós vemos em uma aplicativo, pode ser escrito de diversas formas mas comumente estas telas são escritas em HTML. Uma forma elegante aqui é usar uma linguagem de template que fornece acesso fácio as dados de variáveis.

### O Controle (Control) p No django chamada de view.

Sua aplicação faz alguma coisa, permite interações do usuário, verifica o estado da aplicação, manipula dados e também retornam com os dados necessários a depender da interação destes usuários.

No Django por trabalharmos com a ideia de templates as a expresão View é trocada por Template, e curiosamente o controle (C) é chamado de View (V) assim o MVC do django é o MTV (Model - Template - View).

## Criando uma Aplicação

Uma aplicação django permite visualizar de forma clara o modelo de arquitetura MTV. Para observarmos, vamos construir a primeira aplicação do nosso projeto meusite. E meu site possui um blog onde posso postar algum conteudo. Para criar nossa aplicação vã ao terminal de comandos e execute.

```python
    python3 manage.py startapp blog
```

Aconselho aqui utilizar sua suite preferiada para codificar o seu projeto. Eu irei utilizar o VSCode.

Assim que criamos uma aplicação precisamos pluga-la ao projeto, siga até a pasta do projeto e abra o arquivo settings.py siga atéa variavel INSTALLED_APPS e adcione sua aplicação ao projeto.

```settings.py
    INSTALLED_APPS = [
        ...
        'Blog.apps.BlogConfig'
        ...
    ]
```

Na pasta do seu projeto também tem um arquivo urls.py, que fornece uma forma de criar rotas e manipular o sistema de roteamento da nossa aplicação de forma simples e bastante plugavel. Abra-o e vamos analisa-lo.

Abra a pasta da sua apliacação e vamos procurar entender cada uma das partes de uma aplicação.

O arquivo views.py é onde vamos escrever nossas regras de controle da apliacaçãao. É aqui que codificamos como vemos a apliacação a lista das postagens publicadas, editamos uma postage em especial, podemos apagar entre outras coisas. Vamos criar uma view que receba uma requisição (request) e retorne uma resposta (response). Abra o arquivo views.py e vamos fazer nossa primeira view, que podem ser simples funções python.

```view.py
    from django.shortcuts import render, HTTPResponse    

    def index(request):
        return HTTPResponse('Ola Mundo')
```

No arquivo models.py utilizamos para descrever os atributos dos objetos da nassa aplicação. Na aplicação blog podemos definir um objeto como sendo uma postage. Este objeto tem um titulo, um texto de conteúdo, tem uma data de publicação e quando ele foi atualização, pode ter uma imagem, ou qualquer outros atributos que podem ser abstraido ao objeto. Para construir um modelo utilizamos um pacote do django que permite fazer o mapeamento de um objeto em forma de classe. Para fazer isto vamos importar o pacote models e definir uma classse de modelo que herda a classe Model que permite definir o tipo dos atributos no forma de modelos. Vamos criar uma classe assim:

```models.py
    class Post(models.Model):
        titulo = models.CharField...
        conteudo = models.TextField...
```
