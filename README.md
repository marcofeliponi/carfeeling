<p align="center">
  <img src="https://github.com/user-attachments/assets/d6b8e9f3-4736-4a85-ae80-e516c58d5e31" />
</p>

## Índice

- [Introdução](#introducao)
- [Descrição do Projeto](#descricao-do-projeto)
- [Especificação Técnica](#especificacao-tecnica)
- [Considerações de Design](#consideracoes-de-design)
- [Modelo C4 (Contexto, Contêiner, Componente, Código):](#modelo-c4)
- [Stack Tecnológica](#stack-tecnologica)
- [Considerações de Segurança](#consideracoes-de-seguranca)
- [Backlog do Projeto](#backlog-do-projeto)
- [Requisitos de Software](#requisitos-de-software)
- [Modelagem](#modelagem)
- [Análise de Código](#analise-de-codigo)
- [Monitoramento](#monitoramento)

## Introdução <a id='introducao'></a>

  

Hoje, com o excesso de informação na internet, acaba sendo difícil encontrar avaliações sobre veículos que ajudem a tomar uma decisão de compra, pelo contrário, tantas opções acabam gerando ainda mais dúvida. O projeto Carfeeling surge com a ideia de ser uma ferramenta facilitadora para essa tarefa, oferecendo uma plataforma dedicada a análise com Inteligência Artificial em torno de diferentes modelos de carros nacionais, centralizando feedbacks de especialistas e proprietários comuns de diversos sites em um único local de fácil acesso. O site também disponibiliza um Chat integrado à OpenAI, proporcionando uma IA como uma assistente do usuário. 

  

O Carfeeling almeja facilitar a escolha do carro, ao aplicar técnicas de web scraping e análise de sentimentos para fornecer informações objetivas e que ajudem os usuários. O chat com IA também surge como uma ideia para tirar dúvidas mais específicas, que podem não aparecer na análise inicial.  

  

O objetivo central do projeto é simplificar todo o processo de pesquisa de avaliações e opiniões de carros nacionais, contribuindo para uma maneira mais fácil, prática e eficaz de acessar uma análise concisa e centralizadora. O chat com a Inteligência Artificial também é uma maneira de levar ao público mais leigo em tecnologia uma forma muito simples de utilizar o modelo do GPT para facilitar uma decisão neste contexto, visto que muitos desses usuários não tem o costume de acessar os serviços da OpenAI. 

  

  

  

## Descrição do Projeto <a id='descricao-do-projeto'></a>

  

O Carfeeling é uma plataforma web dedicada à análise de sentimentos da comunidade nacional em torno de modelos de carros, contando também com o Chat com IA. Essa plataforma utiliza técnicas de web scraping para coletar feedbacks de especialistas e proprietários de veículos, consolidando essas informações em uma interface intuitiva para os usuários. Dessa forma, é possível fornecer uma ferramenta de fácil uso e com avaliações e opiniões relevantes sobre o mercado automotivo nacional, auxiliando na tomada de decisão de compra ou até mesmo aluguel de um automóvel.  

  

Alguns problemas a resolver são: a grande variação de informações pela internet, facilitar a tomada de decisão desinformada e precipitada, e a indecisão acerca da grande variedade de veículos disponíveis para compra atualmente.  

  

Como todo projeto, o Carfeeling terá suas limitações, algumas encontradas são:  

  

Disponibilidade de dados limitada, já que o projeto vai estar sujeito às limitações de disponibilidade e acessibilidade de dados online, onde nem todas as fontes de informação podem estar disponíveis para web scraping. Dessa forma, alguns sites mais conhecidos do mundo automotivo serão priorizados no processo de scraping. 

  

Análise limitada a modelos mais conhecidos no mercado, já que o projeto terá mais informações principalmente sobre modelos de carros populares e com grande quantidade de vendas, tendo em vista que modelos não tão conhecidos terão bem menos dados de avaliações disponíveis para web scraping.  

  

Capacidade de processamento do modelo de inteligência artificial e armazenamento de grande quantidade de dados em um modelo MPV, que não possui investimentos de valores no ambiente de produção e usam muito recurso dos serviços Cloud. 

  

Bloqueio de requisições de web scraping pelo Google caso a quantidade de consultas seja grande em pouco tempo. 

  

## Especificação Técnica <a id='especificacao-tecnica'></a>

  

Na parte de Inteligência Artificial o projeto usa modelos relevantes disponibilizados pela biblioteca Transformers Hugging Face, sendo eles 'facebook/bart-large-mnli' para classificação de relevância, e 'nlptown/bert-base-multilingual-uncased-sentiment' para a análise de sentimentos. Os procedimentos são coleta de dados com algoritmos de web scraping, análise através dos Modelos de IA, e armazennamento dos dados coletados são em um formato JSON, contendo informações relevantes sobre o modelo do carro, avaliações coletadas e resultado da análise de sentimento.  

O Carfeeling também conta com alguns serviços integrados: a Parallelum FIPE API para consultar valores FIPE atualizados dos carros consultados, a OpenAI API com o modelo 'gpt-3.5-turbo-0125' para um Chat com Inteligência Artificial, e a Google OAuth para autenticação na plataforma usando uma conta Google.

  

  

## Considerações de Design <a id='consideracoes-de-design'></a>

  

O sistema contará com uma interface limpa, a ideia é que qualquer usuário possa realizar suas consultas de forma prática. Como este projeto exige em sua maior parte funcionalidades que não precisam de muita estilização e componentes front-end, esta parte será a menos complexa.  

  

  


A visão inicial da arquitetura consiste em um front-end desenvolvido em Vue com a responsabilidade de uma usabilidade simples para o usuário, que irá filtrar pelo seu automóvel de interesse, podendo incluir marca, modelo e ano. Assim que a consulta for realizada, a responsabilidade passa a ser do back-end, na linguagem Python, que irá receber parâmetros do front-end e buscar por uma Análise já disponível no Banco de Dados.  

O serviço de Scraping e Análise de Sentimentos ocorre por agendamento, toda segunda-feira de madrugada, para que quando o usuário faça uma consulta os dados já estejam prontos sem demandar uma longa espera. Isso tendo em vista o processo de Análise é demorado e possuímos recursos limitados no ecossitema Google Cloud.  

O serviço criado em Python realiza buscas em websites estratégios, de conteúdos com base na coleção de veículos existente no Banco de Dados Firestore (NoSQL), os conteúdos encontrados no Scraping passam por validações e uso de dois modelos de I.A, o primeiro para manter apenas as partes relevantes do texto, e a segunda para analisar o sentimento. 

Após a coleta de dados acontece a formatação, de forma que possa ser análisado pelos modelos de IA, já o texto original é salvo no Banco de Dados. Desta forma, as análises estarão prontas para consultas no front-end. 

Na parte do Chat, existe uma tela específica para um bate-papo, que realiza requisições para a API do OpenAI integrada ao back-end do Carfeeling. Está API possui uma configuração para conversar mantendo o contexto do veículo passado, funcionando como um assistente do site. Por conta do custo, o Chat terá uma camada de segurança usando a API Google Auth para solicitar login ao usuário. 

  

O projeto é monolítico, já que o back-end contará apenas com Python e é um MVP ainda pequeno, mas que conforme fosse escalando poderia vir a ter microsserviços.  

  

  

  

## Modelo C4 (Contexto, Contêiner, Componente, Código): <a id='modelo-c4'></a> 

  

No contexto deste projeto a arquitetura proposta consiste em um sistema que permite aos usuários filtrarem informações sobre automóveis de interesse, como ano e modelo, obter análises de sentimentos e conversar com uma I.A sobre o veículo desejado. 

  

  

Em relação aos contêineres, teremos o front-end em Vue.js: Responsável pela interface do usuário, oferecendo uma experiência simples e reativa. Este contêiner permite que os usuários filtrem informações sobre os automóveis desejados. No back-end em Python: Este contêiner é encarregado de processar consultas, realizar web scraping em sites para obter dados relevantes, e realizar análises de sentimentos sobre esses dados. Para salvar os registros usa-se o Firestore NoSQL: armazenar os dados obtidos pelo back-end, em forma de objetos nas coleções, facilitando a grande quantidade informações relacionadas e uso do front-end. 

  

  

  

Na parte de Componentes, teremos o Controller (Back-end): Responsável por receber requisições do front-end, processá-las e encaminhá-las para as funções apropriadas. View (Front-end): Apresenta a interface ao usuário, permitindo a interação com os filtros, exibindo os resultados das consultas e uma tela para bate-papo com a IA. Model (Back-end): Consiste nos serviços desenvolvidos em Python, realiza o web scraping, o processamento de dados relevantes, a análise de sentimentos dos dados obtidos e possibilita uma integração com a OpenAI para dúvidas à parte. 

  

  

  

Por último, o código, que como citado anteriormente será desenvolvido em Vue.js no front-end, tendo em vista a facilidade de uso. No back-end o Python, por se destacar em eficiência e praticidade para o contexto do projeto que é Inteligência Artificial. Vale citar o uso do Firestore como database, e toda a hospedagem e Login com o ecossistema Google Cloud. Para a execução do projeto no Cloud Run da Google também se faz necessário o uso de Dockerfile para build. 

  

  

  

## Stack Tecnológica <a id='stack-tecnologica'></a>

  

O projeto conta com uma Stack que favorece o Web Scraping e o uso de I.A. Para isso, é usado Python em todo o back-end por seu grande desempenho neste contexto, e o Firestore NoSQL para um armazenamento dinâmico de diversos dados em uma coleção JSON, que facilita lidar com textos grandes.  

  

No front-end um framework prático e eficaz, o Vue.js, que faz um ótimo trabalho com sua reatividade e possui boas bibliotecas de componentes.  

  

Outras ferramentas utilizadas são GIT e GitHub para versionamento de código, e ecossistema Google Cloud para hospedagem do projeto. Dentro do Google Cloud as ferramentas escolhidas são Cloud Run para execução do front-end e back-end, Firestore para Banco de Dados e Google OAuth para autenticação de usuário. 

  

A gestão das atividades será feita pelo modelo Kanban no software Trello.  

  

  

  

  

  

  

  

## Considerações de Segurança <a id='consideracoes-de-seguranca'></a>

  

Uma das medidas necessárias é o cuidado ao realizar requisições web scraping, para não haver bloqueios. Para isso existem funções de intervalo entre as requisições e diferentes agentes de navegador sendo passados nos headers.

  

Para garantir que a Análise de Sentimento utilize um modelo que forneça bons resultados no contexto de veículos e opiniões, o Carfeeling faz uso de dois bons modelos de IA amplamente conhecidos, disponibilizados pela Hugging Face: "nlptown/bert-base-multilingual-uncased-sentiment" e "facebook/bart-large-mnli". Ambos modelos tiveram um bom desempenho no contexto e não precisaram de fine tuning.

  

Para evitar estresse do sistema e custos exorbitantes no uso do Chat integrado à OpenAI, existe a Autenticação com o Google OAuth.

  

  

  

## Backlog do Projeto  

  

Protótipo das Telas: Desenvolver protótipo das telas que compõem o sistema.  

  

  

  

Estrutura inicial do projeto e versionamento: estrutura de pastas do projeto, pacotes e linguagens/framework utilizados, e versionamento de código ao GitHub.  

  

  

  

Serviço para Web Scraping: Desenvolver serviço que será responsável por entrar nos sites definidos e buscar informações relevantes sobre os veículos.   

Sites: Quatro Rodas, Carros na Web, iCarros, FlatOut, Na Pista, Auto Entuasiastas  

  

  

  

Serviço para Análise de Sentimentos: Desenvolver serviço back-end responsável por processar as informações conseguidas com Web Scraping. Esse serviço deverá rodar em Python e processar a informação de modo que seja possível salvar no Banco de Dados resultados já formatados para o posteriormente serem consultados.  

  

  

  

Design do Banco de Dados: Definir coleções usadas no Firestore. 

  

  

Conexão com Banco de Dados: Conectar e configurar a conexão do projeto ao Firestore.  

  

  

Tela inicial para consultar análises: Desenvolver tela inicial do sistema, que possibilita realizar as consultas de análises.  

  

  

Configuração de ambiente oficial: Configurar ambiente para hospedar o sistema. Principal opção é o Google Cloud.  

  

  

Configuração de CI/CD: Integração contínua para atualizar o projeto no ambiente oficial.  

  

  

API para consultar os veículos: Construir API que será usada para buscar as avaliações do veículo.  

Deve aceitar tanto consultas gerais quanto as com filtros.  

Será uma rota GET com path params recebendo o veículo, filtros opcionais devem ser definidos como query params.  

  

  

Componente front-end de avaliações: Componente para mostrar a média de nota do veículo consultado. Possível usar componentes já disponibilizados por bibliotecas relevantes.  

  

  

Automação de serviços do produto: Agendamento diário para realizar todo o processo que obtêm novas análises para o sistema. Ou seja, durante a madrugada de cada dia será executado o serviço para realizar web scraping, analisar os sentimentos, tratar as informações e indexar no banco de dados. Dessa forma sempre teremos dados prontos para serem buscados a cada consulta de um usuário.  

  

  

  

  

Tela para chat com a Inteligência Artificial: Desenvolver tela para conversar com a assistente integrada via API da OpenAI, essa tela obrigatoriamente irá solicitar login através do Google. 

  

  

  

## Requisitos de Software  

  

### Requisitos Funcionais:  

  

#### RF1 - Consultar por automóveis de interesse, de forma filtrada ou não:
O sistema deve permitir que os usuários realizem consultas de análises fornecendo parâmetros de marca, modelo e ano do veículo.


  

#### RF2 - Visualizar as fontes usadas para gerar a análise do veículo:
O usuário poderá em cada consulta de veículo visualizar os sites que foram usados como fonte para web scraping e análise de inteligência artificial. Essas fontes podem variar de acordo com a análise.

  

#### RF3 - Visualizar pontos positivos e negativos do veículo durante a consulta:
Em cada consulta a análise gerada disponibilizará ao usuário uma tela mostrandos pontos os positivos e negativos do veículo em questão, com informações vindas do web scraping.


#### RF4 - Visualizar o valor de tabela FIPE do veículo:
Cada consulta busca em tempo real o valor FIPE do veículo através de uma API integrada, o usuário deve visualizar essa informação em todas as consulta. Caso o valor não seja encontrado na API, será exibido um valor existente na base de dados.
  

#### RF5 - Comparar o veículo consultado com outros veículos de faixa de preço semelhante:
Durante uma consulta o usuário deve ter a opção de visualizar como a nota geral do veículo consultado está em relação à outros 3 veículos com uma faixa de preço parecida.


#### RF6 - Autenticação com integração do Google:
O usuário tem a opção de se autenticar-se usando a API de Integração Google OAuth.


#### RF7 - Chat com Assistente de Inteligência Artificial.
Após autenticado, o usuário pode iniciar um chat com uma IA Assistente para tirar dúvidas sobre um veículo específico.



### Requisitos Não Funcionais:  

  

#### RNF1 - Garantir um uso intuitivo da aplicação:
O sistema deve ser fácil e prático, com interface intuitiva.

  

#### RNF2 - Assegurar velocidade na resposta das consultas, proporcionando alto desempenho:
O sistema precisa ter respostas rápidas em todas as telas, desde às consultas de análises até o chat com IA.

  

#### RNF3 - Proporcionar análises precisas e dados relevantes:
O sistema de scraping e análise de IA deve manter dados que façam sentido com o contexto da consulta, apenas com informações relevantes.


#### RNF4 - Análises atualizadas semanalmente:
O sistema deve realizar novos scrapings e análises de sentimentos toda segunda-feira, às 00:00h.

#### RNF5 - Chat útil com Assistente de Inteligência Artificial:
O chat disponiblizado no sistema deve ser adaptado ao contexto do site e proporcionar uma conversa relevante, esclarecendo dúvidas do usuário sobre o veículo escolhido.

#### RNF6 - Escalabilidade:
O sistema deve estar apto à escalabilidade vertical no ecossistema Google Cloud, no Firestore e também Cloud Run.

#### RNF7 - Disponibilidade:
O sistema deve estar disponível em produção todos os dias da semana, 24 horas por dia.

#### RNF8 - Tolerância a falhas:
O sistema deve continuar funcionando mesmo que a API de terceiros (como a FIPE Parallelum) esteja indisponível, usando informações previamente armazenadas.


## Modelagem

Para a organização de backlog e tarefas à serem desenvolvidas foi utilizada a ferramenta Trello.


## Análise de Código <a id='analise-de-codigo'></a>

Eslint para front-end Vue:

![eslint (analise de codigo)](https://github.com/user-attachments/assets/04a5ea94-c93f-4ef1-845e-124c34b2ca4a)

Pylint para back-end Python:

![pylint (analise de codigo)](https://github.com/user-attachments/assets/650feb56-899f-40dc-8b46-58423060d003)


## Monitoramento

O ecossistema GCloud disponibiliza um produto integrado para monitoramento/observabilidade, visto que o sistema Carfeeling está hospedado nos serviços GCloud.

Front-end:

![monitoramento (web)](https://github.com/user-attachments/assets/30843f16-e2a8-45c2-95b2-d8302a512b5e)

Back-end:

![image](https://github.com/user-attachments/assets/7e89215f-051e-4343-9e38-edbea886ffc5)

