## Introdução 

Nos dias de hoje, os consumidores enfrentam um desafio grande ao buscar informações confiáveis sobre modelos específicos de carros, já que as opções são muitas. Com a grande quantidade de opiniões diferentes em redes sociais e fóruns, encontrar uma análise que seja confiável pode ser uma tarefa difícil. O projeto Car Feeling surge como uma solução para esse problema, oferecendo uma plataforma dedicada a analisar o sentimento em torno de diferentes modelos de carro, consolidando feedbacks de especialistas e proprietários em um único local de fácil acesso. 

O Car Feeling pretende desempenhar um papel importante ao aplicar técnicas avançadas de web scraping e análise de sentimentos para fornecer informações valiosas aos usuários, a ideia é implicar bastante na vida do usuário tendo em vista que comprar um veículo é um custo muito alto na nossa situação socioeconômica. Ao simplificar esse processo de pesquisa e junção de feedbacks de carros, o Car Feeling contribui para a eficiência das decisões de compra ou aluguel de automóveis. 

O objetivo central do projeto Car Feeling é proporcionar aos usuários uma maneira fácil e eficaz de acessar avaliações e opiniões sobre os carros de seu interesse, e o melhor, de forma prática e rápida.  

 

## Descrição do Projeto 

O projeto Car Feeling visa desenvolver uma plataforma online dedicada à análise do sentimento da comunidade em torno de modelos específicos de carro. Essa plataforma irá utilizar técnicas avançadas de web scraping para coletar feedbacks de especialistas e proprietários de veículos, consolidando essas informações em uma interface intuitiva e acessível aos usuários. A principal finalidade do projeto é fornecer aos consumidores uma fonte confiável e abrangente de avaliações e opiniões sobre os carros de seu interesse, auxiliando-os na tomada de decisões informadas sobre a compra ou aluguel de um automóvel. 

Alguns problemas a resolver são a falta de informações consolidadas para o consumidor, a tomada de decisão desinformada e precipitada e a indecisão acerca da grande variedade de veículos disponíveis no mercado no dia de hoje. 

Como todo projeto, o Car Feeling terá suas limitações, algumas já previstas são: 

Disponibilidade de dados limitada, já que o projeto vai estar sujeito às limitações de disponibilidade e acessibilidade de dados online, onde nem todas as fontes de informação podem estar disponíveis para web scraping. 

Análise limitada a modelos mais conhecidos no mercado, já que o projeto terá mais informações principalmente sobre modelos de carros populares e com grande quantidade de vendas, já que modelos não tão conhecidos terão bem menos dados de avaliações disponíveis para web scraping. 

 

## Especificação Técnica 

O projeto Car Feeling irá usar para análise de sentimento algoritmos baseados em Inteligência Artificial, com métodos capazes de filtrar dados relevantes. Os procedimentos incluirão a definição de uma estratégia de coleta de dados, a implementação de algoritmos de web scraping, o desenvolvimento da interface de usuário e testes de funcionalidade e desempenho. Os dados coletados serão armazenados em um formato JSON, contendo informações relevantes sobre o modelo do carro, avaliações coletadas e resultado da análise de sentimento. 

 

## Considerações de Design 

O projeto contará com uma interface limpa, a ideia é que qualquer usuário possa realizar suas consultas de forma prática. Já que este projeto exige em sua maior parte funcionalidades que não precisam de muita estilização e componentes front-end, esta parte será a menos complexa. 

 

A visão inicial da arquitetura consiste em um front-end com a responsabilidade de uma usabilidade simples para o usuário, que irá filtrar pelo seu automóvel de interesse, podendo incluir ano, modelo, entre outros detalhes. Assim que a consulta for realizada, a responsabilidade passa a ser do back-end, primeiramente na linguagem Golang, que irá receber parâmetros recebidos do front-end e começar a realizar o web scraping. O serviço criado em Golang irá buscar em diversos websites assuntos relacionados aos filtros e que possam ser entendidos pela máquina como sentimentos. 
Com a coleção de vários dados acontecerá a formatação, de forma que possa ser passado para nosso outro serviço, criado em Python. Nessa parte do código o objetivo será realizar a análise de sentimentos dos dados, com o uso de Inteligência Artificial, podendo assim interpretar o que a maior parte do público sente a respeito do veículo. 
Após todo esse processo, o resultado será indexado e salvo no Elastic Search, para serem usados novamente em buscas que sejam iguais em uma data não tão distante, visto que o sentimento pode mudar com o tempo, e depois de todo esse processo os resultados serão retornados ao front-end para visualização do usuário. 

 

Como a maioria das aplicações Web o projeto consistirá com um modelo MVC, onde o Controller se comunicará com a View e posteriormente com o Model do back-end. Também contará com uma arquitetura de microsserviços, visto que o back-end contará com a linguagem Golang e Python, tornando a divisão de ambas as linguagens mais limpas e concisas, separando as responsabilidades. 

 

## Modelo C4 (Contexto, Contêiner, Componente, Código):  

No contexto deste projeto a arquitetura proposta consiste em um sistema que permite aos usuários filtrarem informações sobre automóveis de interesse, como ano e modelo, e obter análises de sentimentos relacionadas a esses veículos. 

 
Em relação aos contêineres, teremos o front-end em Vue.js: Responsável pela interface do usuário, oferecendo uma experiência simples e reativa. Este contêiner permite que os usuários filtrem informações sobre os automóveis desejados. No back-end em Golang e Python: Dividido em microsserviços, este contêiner é encarregado de processar consultas, realizar web scraping em diversos sites para obter dados relevantes, e realizar análises de sentimentos sobre esses dados. Utiliza Golang para a velocidade do web scraping e Python para a análise de sentimentos. E por último o Elasticsearch: Utilizado para indexar e armazenar os dados obtidos pelo back-end, garantindo rápida recuperação e acesso eficiente para consultas futuras. 

 

Na parte de Componentes, teremos o Controller (Back-end): Responsável por receber requisições do front-end, processá-las e encaminhá-las para os microsserviços apropriados. View (Front-end): Apresenta a interface ao usuário, permitindo a interação com os filtros e exibindo os resultados das consultas. Model (Back-end): Consiste nos microsserviços desenvolvidos em Golang e Python. O serviço em Golang realiza o web scraping e o serviço em Python realiza a análise de sentimentos dos dados obtidos. 

 

Por último, o código, que como citado anteriormente será desenvolvido em Vue.js no front-end, tendo em vista a facilidade de uso. No back-end o Golang e Python, por se destacarem em velocidade e eficiência para o contexto do projeto. Vale citar novamente o uso do Elasticsearch como database, deploys com Git Flow e hospedagem com Google Cloud. 

 

## Stack Tecnológica 

A ideia é que o projeto conte com uma Stack que favoreça o Web Scrapping e a análise de sentimentos de uma forma otimizada e eficaz. Para isso, será usado Golang na realização do Web Scraping, já que é uma linguagem muito conhecida por sua velocidade, Python para a realização da análise de sentimentos dos dados encontrados, e o Elastic Search para indexação e armazenamento dos dados. 

Já no front-end busquei por um framework que tenho maior afinidade, o Vue.js, e que faz um ótimo trabalho com sua reatividade. 

Outras ferramentas utilizadas serão GIT e GitHub para versionamento de código, Git Flow para deploys, e Google Cloud para hospedagem do projeto. 

A gestão das atividades será feita pelo modelo Kanban no software Trello. 

 

 

 

## Considerações de Segurança 

Uma das medidas necessárias será o cuidado ao realizar requisições para web scraping, para não ser identificado como um bot, e para os dados coletados não gerarem problemas no nosso sistema com algum tipo de injeção.  

Será ideal garantir que a Análise de Sentimento não fique viciada ou sofra algum tipo de viés em seus resultados. 

Para evitar estresse do sistema ou possíveis ataques se fará necessário uma Limitação de Taxa, para que um único usuário não envie muitas solicitações em um curto período. Implementações de Captcha também podem ajudar nesse aspecto. 

 

## Backlog do Projeto 

Protótipo das Telas: Desenvolver protótipo no Figma das telas que compõem o sistema. 

 

Estrutura inicial do projeto e versionamento: estrutura de pastas do projeto, pacotes e linguagens/framework utilizados, e versionamento de código ao GitHub. 

 

Serviço para Web Scraping: Desenvolver serviço que será responsável por entrar nos sites definidos e buscar informações relevantes sobre os veículos.  
Sites: Quatro Rodas, Carros na Web, iCarros, FlatOut, Na Pista, Auto Entuasiastas 

 

Serviço para Análise de Sentimentos: Desenvolver serviço back-end responsável por processar as informações conseguidas com Web Scraping. Esse serviço deverá rodar em Python e processar a informação de modo que seja possível salvar no Banco de Dados resultados já formatados para o posteriormente serem consultados. 

 

Design do Banco de Dados: Definir arquitetura da tabela no Elastic Search 
 

Conexão com Banco de Dados: Conectar e configurar a conexão do projeto ao Elastic Search. 
 

Tela inicial para consultar análises: Desenvolver tela inicial do sistema, que possibilita realizar as consultas de análises. 
 

Configuração de ambiente oficial: Configurar ambiente para hospedar o sistema. Principal opção é o Google Cloud. 
 

Configuração de CI/CD: Integração contínua para atualizar o projeto no ambiente oficial. 
 

 API para consultar os veículos: Construir API que será usada para buscar as avaliações do veículo. 
Deve aceitar tanto consultas gerais quanto as com filtros. 
Será uma rota GET com path params recebendo o veículo, filtros opcionais devem ser definidos como query params. 
 

 Componente front-end de avaliações: Componente para mostrar a média de nota do veículo consultado. Possível usar componentes já disponibilizados por bibliotecas relevantes. 
 

 Automação de serviços do produto: Agendamento diário para realizar todo o processo que obtêm novas análises para o sistema. Ou seja, durante a madrugada de cada dia será executado o serviço para realizar web scraping, analisar os sentimentos, tratar as informações e indexar no banco de dados. Dessa forma sempre teremos dados prontos para serem buscados a cada consulta de um usuário. 
 

 Cobertura de Testes: Implementar testes de software no projeto. 
 

 API para feedbacks: Desenvolver rota que irá salvar opiniões do usuário sobre o site como um todo ou sobre o resultado da consulta. 
 

 Tela para feedbacks: Desenvolver tela para feedback do sistema. Essa tela deverá ser mostrada após o usuário realizar alguma consulta. 

 

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
