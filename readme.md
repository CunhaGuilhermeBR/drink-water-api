## drinkWater API

A drinkWater API é uma api feita para lembrar o usuário de beber água todos os dias e ter um controle maior de como está indo sua evolução.

## 🚀 Preparando e executando a aplicação 🚀

O projeto utiliza Python(3.11.4) como linguaguem e o Django(4.2.3) como framework. É necessário ter o Insonmia, Postman ou semelhantes para chamar as rotas da API e ter acesso aos recursos.

O projeto está disponível em: https://github.com/CunhaGuilhermeBR/drink-water-api

### Executando a aplicação

Para rodar basta ir a pasta de origem do projeto e rodar o comando

```
  ~ python manage.py runserver
```

## 🚀 RoadMap de melhorias 🚀 

1. Múltiplos routers/urls para o app 'users'.</br>
    1.1. Motivo: Não tive conhecimento o bastante e nas minhas pesquisas não encontrei como fazer, apenas dava erro e então decidi por usar apenas um router</br>
    1.2. Impacto: Quebra do príncipio de responsabilidade única, deixa o código mais feio e mais complicado de dar manutenção.</br>

2. Criação de rotinas.</br>
    2.1. Motivo: Não tive conhecimento o bastante e nas minhas pesquisas não encontrei como fazer, apenas dava erro e então decidi pela solução de criar a instância do dia quando o usuário adiciona e não encontra, então ele consegue fazer o controle.</br>
    2.2. Impacto: Na minha concepção uma rotina de criação de uma instância para cada usuário é uma solução mais "elegante" e que atende melhor os requisitos.</br>


### Links

Rodando a aplicação no Insonmia: https://drive.google.com/file/d/1uEEYq25ltkwKXogyWhLz3t5mUwa-HnXv/view?usp=sharing

Arquitetura e decisões técnicas: https://drive.google.com/file/d/1cG-kHZ9M6jjOK6vUD5qQVzmfiHz2lUpY/view?usp=sharing