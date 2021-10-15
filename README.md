# Exercício Instruct The Women 👩‍💻

Neste repositório você encontra o enunciado do exercício técnico para a vaga de
trainee do programa [Instruct The Women](https://instruct.com.br/trabalhe-com-a-gente/instruct-the-women/) organizado pela [Instruct](https://instruct.com.br/) em
parceria com a [Se Candidate, Mulher!](https://secandidatemulher.com.br/).

Para saber mais sobre a empresa, leia o [FAQ](#FAQ)

## Requisitos

* Possuir uma conta no GitHub
* Navegador Chrome ou Firefox
* Familiaridade com VS Code

## O que é importante você saber

* Conhecer HTTP e APIs Rest
* Saber sobre métodos HTTP como GET, POST e DELETE
* Conhecer sobre JSON e estruturas como listas e dicionários (*Arrays* e *Objects*)

## Ambiente de Desenvolvimento

Para esse exercício vamos utilizar um ambiente totalmente no browser e que não
requer nenhuma instalação em seu computador.

É possível fazer o exercício localmente no seu computador. Nesse caso, a configuração
de ferramentas para desenvolvimento é de sua responsabilidade e não temos como ajudar
todas as participantes.

### Faça um fork

Primeiro, crie um fork deste repositório com sua conta no GitHub.

Em termos simples, um fork é cópia de um repositório. Leia a
[documentação do GitHub](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
para saber mais.

A partir de agora, todas as ações devem ser feitas no seu fork!

Ele estará disponível dessa forma: `https://github.com/SEU_LOGIN/instruct-the-women-2021`

### Usando o browser (recomendado)

Abra o seu fork em uma aba do seu browser.

Você estará na **sua cópia** do repositório original.

Então, na **sua cópia** do repositório aberta, clique no botão abaixo:   

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/from-referrer/)

Você será redirecionada para o gitpod.io e será necessário criar uma conta gratuita usando sua conta do GitHub.

Uma janela será aberta solicitando que você autorize o gitpod.io a acessar sua conta do GitHub.

Após a confirmação da solicitação de autorização, uma instância do VS Code será criada para você.

Aguarde alguns instantes, cerca de 2 a 3 minutos até o término do carregamento do ambiente.

### Usando seu computador (avançado)

| ⚠️ | Não temos como ajudar caso a caso as participantes na configuração de um ambiente de desenvolvimento. Se você não se sentir segura, use o ambiente pronto no browser que preparamos. |
| --- | --- |

Caso já tenha experiência, também é possível clonar este repositório git no
seu computador e desenvolver em ambiente local. Os requisitos são:

- Python 3.8
- pipenv
- Bibliotecas de desenvolvimento para PostgreSQL (libpq-dev)

Você vai precisar também do [k6](https://k6.io/) para testar seu projeto. Para instalar o k6
basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu
sistema operacional (Windows, Linux ou Mac).

E para fazer o deploy quando terminar, é necessário instalar o [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Se você está num computador com Windows, é recomendado 
[seguir o tutorial da Microsoft](https://docs.microsoft.com/en-us/windows/python/web-frameworks)
para configurar um ambiente de desenvolvimento com WSL.

## O problema

A equipe de desenvolvimento _Bleeding Edge Enthusiasts_ (BEE) se orgulha de 
usar as tecnologias mais recentes e modernas. Essa regra também se aplica aos
projetos desenvolvidos em Python pela equipe BEE.

Quando uma funcionalidade não existe nativamente no interpretador Python, a equipe
faz uso dos chamados **pacotes**. De maneira simples, um pacote é um conjunto de
códigos prontos para serem usados por qualquer pessoa e que facilitam o desenvolvimento.

Para garantir que todos seus projetos em Python estão usando as últimas versões
disponíves dos pacotes, a equipe pensou em criar uma ferramenta batizada de 
MagPy. A ferramenta recebe um nome de projeto, uma lista de pacotes e devolve a 
última versão de cada pacote.

Um dos integrantes da BEE apontou que a 
[API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html)
poderia ser usada para esse fim.

## Solução

Você deve desenvolver a MagPy, uma API REST que gerencia uma coleção de 
projetos, sendo:

* Cada projeto tem um nome e uma lista de pacotes.
* Cada pacote tem um nome e uma versão.

O cadastro de um projeto recebe o nome e a lista de pacotes. Cada pacote da 
lista precisa obrigatoriamente especificar um nome, mas a versão é opcional.

Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
nome e a versão do pacote.

Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
a última versão publicada no [PyPI](https://pypi.org/).

Abaixo, alguns exemplos de chamadas que serão feitas nessa API:

```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```
O código HTTP de retorno deve ser 201 e o corpo esperado na resposta é:
```
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},  // Usou a versão mais recente
        {"name": "graphene", "version": "2.0"}   // Manteve a versão especificada
    ]
}
```

Se um dos pacotes informados não existir, ou uma das versões especificadas for
inválida, um erro deve ser retornado.

Para uma chamada semelhante ao exemplo abaixo:
```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "pypypypypypypypypypypy"},
        {"name": "graphene", "version": "1900"}
    ]
}
```
O código HTTP de retorno deve ser 400 e o corpo esperado na resposta é:
```
{
    "error": "One or more packages doesn't exist"
}
```

Também deve ser possível visitar projetos previamente cadastrados, usando o
nome na URL:
```
GET /api/projects/titan
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```

E deletar projetos pelo nome:
```
DELETE /api/projects/titan
```

| ⚠️ | Sua solução deve usar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html). Não use outro caminho pra buscar as informações necessárias |
| --- | --- |


## Implementação

Este repositório tem parte da solução implementada e você deve continuar para
que o projeto atenda a especificação descrita acima. Também está adiantado
algumas configurações para publicação do projeto no 
[Heroku](https://www.heroku.com/). Este projeto usa principalmente
[Django](https://www.djangoproject.com/) e
[Django REST framework](https://www.django-rest-framework.org/).

O projeto tem as assinaturas de algumas funções e métodos para orientar uma 
solução, mas você pode alterar o código à vontade, desde que a solução final
passe nos testes. Mais detalhes sobre isso na seção "Avaliação" do README.

As funções e métodos para implementar estão em 2 arquivos:
- `api/pypi.py`
- `api/serializers.py`

Em `api/pypi.py` você escreverá algumas funções para fazer a integração com a
API do PyPI. Essas funções serão úteis para validar os dados recebidos pela API
desenvolvida.

Em `api/serializers.py` falta implementar a persistência dos dados e usar
as funções criadas em `api/pypi.py` para a validar os dados.

## Validando seu projeto

Nesse exercício incluímos testes usando a ferramenta [k6](https://k6.io/). Com ela é possível
testar o comportamento da API e validar se tudo está funcionando de acordo com
a especificação.

Os testes básicos estão disponíveis neste repositório no arquivo
`tests-open.js`. Use-os durante o desenvolvimento para avaliar se a sua API está correta.

Para rodar os testes, especifique a variável de ambiente "API_BASE"
com o endereço base da API testada e no editor do gitpod.io, abra um novo
terminal para executar o comando abaixo.

Exemplo de aplicação rodando no localhost na porta 8000:
```
k6 run -e API_BASE='http://localhost:8000/' tests-open.js
```

## Fazendo deploy

1. Crie uma conta gratuita no [Heroku](https://signup.heroku.com/)
2. Na página [Account Settings](https://dashboard.heroku.com/account) role até "API Key" e clique em "reveal"
3. No editor do gitpod.io, abra um novo Terminal.
4. Autentique-se com `heroku login -i` digite o e-mail da sua conta. No lugar da senha, digite o valor que você conseguiu no passo 2.
5. No terminal digite `heroku create` para criar sua aplicação
6. No terminal digite `git push heroku` para fazer o deploy
7. No [dashboard do Heroku](https://dashboard.heroku.com/apps) entre no app que foi criado pelo passo anterior
8. Na aba "Access" clique em "Add collaborator" e preencha com o e-mail `jobs@instruct.com.br`

Pronto! Seu projeto foi publicado e a Instruct tem acesso para avaliá-lo!

Quando finalizar a implementação, adicione o usuário com e-mail
`jobs@instruct.com.br` como colaborador do app publicado até o fim do prazo
estipulado. Isso nos garante acesso ao endereço em que sua API está publicada,
para seguir com os testes automatizados.

| ⚠️ | Você deve adicionar o usuário com e-mail `jobs@instruct.com.br` no app publicado no Heroku! Não é necessário adicionar acesso ao código fonte num repositório do GitHub. |
| --- | --- |

Se você conseguiu chegar até aqui, parabéns!

## Avaliação (opcional)

Caso você tenha feito o deploy no Heroku com sucesso, poderemos avaliar seu código!

Nós executaremos dois conjuntos de testes na sua API:

1. Testes básicos (iguais aos que estão no repositório usando `k6`)
2. Testes avançados (fechados)

Sua API deve passar ao menos nos testes básicos para avaliarmos.

**Boa sorte!**

---

## FAQ

### Como me candidatar para trabalhar na Instruct?

As inscrições são feitas através das vagas publicadas no site: https://instruct.com.br/trabalhe-com-a-gente/

Nessa página estão listadas as vagas abertas e todos os detalhes de nosso
processo seletivo.

### Como ser avisada de novas vagas?

[Siga a Instruct no Linkedin](https://www.linkedin.com/company/instructbr).

Sempre publicamos quando novas vagas são abertas.

### Como é trabalhar na Instruct?

Você pode ler nosso [Handbook](https://github.com/instruct-br/handbook). 
Ele é a referência completa sobre como a Instruct funciona.

Destaque especial para as atribuições do papel de [Analista de Desenvolvimento Trainee](https://github.com/instruct-br/handbook/blob/main/papeis.md#analista-de-desenvolvimento-trainee)
