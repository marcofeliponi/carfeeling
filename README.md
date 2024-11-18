![logo](https://github.com/user-attachments/assets/d6b8e9f3-4736-4a85-ae80-e516c58d5e31)



## Introdução  

  

Hoje, com o excesso de informação na internet, acaba sendo difícil encontrar avaliações sobre veículos que ajudem a tomar uma decisão de compra, pelo contrário, tantas opções acabam gerando ainda mais dúvida. O projeto Carfeeling surge com a ideia de ser uma ferramenta facilitadora para essa tarefa, oferecendo uma plataforma dedicada a análise com Inteligência Artificial em torno de diferentes modelos de carros nacionais, centralizando feedbacks de especialistas e proprietários comuns de diversos sites em um único local de fácil acesso. O site também disponibiliza um Chat integrado à OpenAI, proporcionando uma IA como uma assistente do usuário. 

  

O Carfeeling almeja facilitar muito a escolha do carro, ao aplicar técnicas de web scraping e análise de sentimentos para fornecer informações objetivas e que ajudem os usuários. O chat com IA também surge como uma ideia para tirar dúvidas mais específicas, que podem não aparecer na análise inicial.  

  

O objetivo central do projeto é simplificar todo o processo de pesquisa de avaliações e opiniões de carros nacionais, contribuindo para uma maneira mais fácil, prática e eficaz de acessar uma análise concisa e centralizadora. O chat com a Inteligência Artificial também é uma maneira de levar ao público mais leigo em tecnologia uma forma muito simples de utilizar o modelo do GPT para facilitar uma decisão neste contexto, visto que muitos desses usuários não tem o costume de acessar os serviços da OpenAI. 

  

  

  

## Descrição do Projeto  

  

O projeto Carfeeling terá uma plataforma web dedicada à análise de sentimentos da comunidade nacional em torno de modelos de carro, contando também com o Chat com IA. Essa plataforma irá utilizar técnicas de web scraping para coletar feedbacks de especialistas e proprietários de veículos, consolidando essas informações em uma interface intuitiva para os usuários. Dessa forma, é possível fornecer uma ferramenta de fácil uso e com avaliações e opiniões relevantes sobre o mercado automotivo nacional, auxiliando na tomada de decisão de compra ou até mesmo aluguel de um automóvel.  

  

Alguns problemas a resolver são: a grande variação de informações pela internet, facilitar a tomada de decisão desinformada e precipitada, e a indecisão acerca da grande variedade de veículos disponíveis para compra atualmente.  

  

Como todo projeto, o Carfeeling terá suas limitações, algumas já previstas são:  

  

Disponibilidade de dados limitada, já que o projeto vai estar sujeito às limitações de disponibilidade e acessibilidade de dados online, onde nem todas as fontes de informação podem estar disponíveis para web scraping. Dessa forma, alguns sites mais conhecidos do mundo automotivo serão priorizados no processo de scraping. 

  

Análise limitada a modelos mais conhecidos no mercado, já que o projeto terá mais informações principalmente sobre modelos de carros populares e com grande quantidade de vendas, tendo em vista que modelos não tão conhecidos terão bem menos dados de avaliações disponíveis para web scraping.  

  

Capacidade de processamento do modelo de inteligência artificial e armazenamento de grande quantidade de dados em um modelo MPV, que não possui investimentos de valores no ambiente de produção e usam muito recurso dos serviços Cloud. 

  

Bloqueio de requisições de web scraping pelo Google caso a quantidade de consultas seja grande em pouco tempo. 

  

## Especificação Técnica  

  

O projeto irá usar para a análise de sentimentos modelos de Inteligência Artificial relevantes e amplamente conhecidos, com métodos capazes de filtrar dados relevantes. Os procedimentos incluirão a definição de uma estratégia de coleta de dados, a implementação de algoritmos de web scraping, o desenvolvimento da interface visual e um chat integrado com a OpenAI. Os dados coletados serão armazenados em um formato JSON, contendo informações relevantes sobre o modelo do carro, avaliações coletadas e resultado da análise de sentimento.  

  

  

  

## Considerações de Design  

  

O sistema contará com uma interface limpa, a ideia é que qualquer usuário possa realizar suas consultas de forma prática. Como este projeto exige em sua maior parte funcionalidades que não precisam de muita estilização e componentes front-end, esta parte será a menos complexa.  

  

  

  

A visão inicial da arquitetura consiste em um front-end desenvolvido em Vue com a responsabilidade de uma usabilidade simples para o usuário, que irá filtrar pelo seu automóvel de interesse, podendo incluir marca, modelo e ano. Assim que a consulta for realizada, a responsabilidade passa a ser do back-end, na linguagem Python, que irá receber parâmetros recebidos do front-end e buscar por uma Análise já disponível no Banco de Dados.  

O serviço de Scraping e Análise de Sentimentos ocorrerá por agendamento, em um horário de baixo pico, para que quando o usuário faça uma consulta os dados já estejam prontos e sem demandar de uma longa espera.  

O serviço criado em Python irá buscar em websites conteúdos com base na coleção de veículos salva no Banco de Dados Firestore (NoSQL), os conteúdos encontrados no Scraping irão passar por validações e uso de dois modelos de I.A, o primeiro para manter apenas as partes relevantes do texto, e a segunda para analisar o sentimento. 

Com a coleção de vários dados acontecerá a formatação, de forma que possa ser salvo no Banco de Dados. Desta forma, as análises estarão salvas para consultas no front-end. 

Já na parte do Chat, haverá uma tela específica para um bate-papo, que fará requisições para a API do OpenAI. Está API terá uma configuração para assuntos apenas relacionadas ao veículo passado, funcionando como um assistente do site.  

Por conta do custo, o Chat terá uma camada de segurança usando a API Google Auth para solicitar login ao usuário. 

  

O projeto usará um modelo MVC, onde o Controller se comunicará com a View e posteriormente com o Model do back-end. Isso estará arquitetado em monolito, visto que o back-end contará apenas com Python e é um MVP, mas que conforme fosse escalando poderia vir a ter microsserviços.  

  

  

  

## Modelo C4 (Contexto, Contêiner, Componente, Código):   

  

No contexto deste projeto a arquitetura proposta consiste em um sistema que permite aos usuários filtrarem informações sobre automóveis de interesse, como ano e modelo, obter análises de sentimentos e conversar com uma I.A sobre o veículo desejado. 

  

  

Em relação aos contêineres, teremos o front-end em Vue.js: Responsável pela interface do usuário, oferecendo uma experiência simples e reativa. Este contêiner permite que os usuários filtrem informações sobre os automóveis desejados. No back-end em Python: Este contêiner é encarregado de processar consultas, realizar web scraping em sites para obter dados relevantes, e realizar análises de sentimentos sobre esses dados. Para salvar os registros usa-se o Firestore NoSQL: armazenar os dados obtidos pelo back-end, em forma de objetos nas coleções, facilitando a grande quantidade informações relacionadas e uso do front-end. 

  

  

  

Na parte de Componentes, teremos o Controller (Back-end): Responsável por receber requisições do front-end, processá-las e encaminhá-las para as funções apropriadas. View (Front-end): Apresenta a interface ao usuário, permitindo a interação com os filtros, exibindo os resultados das consultas e uma tela para bate-papo com a IA. Model (Back-end): Consiste nos serviços desenvolvidos em Python, realiza o web scraping, o processamento de dados relevantes, a análise de sentimentos dos dados obtidos e possibilita uma integração com a OpenAI para dúvidas à parte. 

  

  

  

Por último, o código, que como citado anteriormente será desenvolvido em Vue.js no front-end, tendo em vista a facilidade de uso. No back-end o Python, por se destacar em eficiência e praticidade para o contexto do projeto que é Inteligência Artificial. Vale citar o uso do Firestore como database, e toda a hospedagem e Login com o ecossistema Google Cloud. Para a execução do projeto no Cloud Run da Google também se faz necessário o uso de Dockerfile para build. 

  

  

  

## Stack Tecnológica  

  

A ideia é que o projeto conte com uma Stack que favoreça o Web Scraping e o uso de I.A. Para isso, será usado Python em todo o back-end por seu grande desempenho neste contexto, e o Firestore NoSQL para um armazenamento dinâmico de diversos dados.  

  

Já no front-end um framework prático e eficaz, o Vue.js, que faz um ótimo trabalho com sua reatividade.  

  

Outras ferramentas utilizadas serão GIT e GitHub para versionamento de código, e ecossistema Google Cloud para hospedagem do projeto. Dentro do Google Cloud as ferramentas escolhidas são Cloud Run para execução do front-end e back-end, Firestore para Banco de Dados e Google OAuth para autenticação de usuário. 

  

A gestão das atividades será feita pelo modelo Kanban no software Trello.  

  

  

  

  

  

  

  

## Considerações de Segurança  

  

Uma das medidas necessárias será o cuidado ao realizar requisições para web scraping, para não ser identificado como um bot.   

  

Será ideal garantir que a Análise de Sentimento utilize um modelo que forneça bons resultados no contexto de veículos e opiniões.  

  

Para evitar estresse do sistema, principalmente no uso do Chat integrado à OpenAI, será necessário sistema de Autenticação com o Google OAuth.  

  

  

  

## Backlog do Projeto  

  

Protótipo das Telas: Desenvolver protótipo no Figma das telas que compõem o sistema.  

  

  

  

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

  

Consultar por automóveis de interesse, de forma filtrada ou não.  

  

Visualizar as fontes usadas para o resultado apresentado.  

  

Avaliar o resultado ou o site como um todo.  

  

### Requisitos Não Funcionais:  

  

Garantir um uso intuitivo da aplicação.  

  

Assegurar velocidade na resposta das consultas, proporcionando desempenho.  

  

Proporcionar análises precisas e dados relevantes.  

  

Manter informações atualizadas diariamente através de agendamentos. 
