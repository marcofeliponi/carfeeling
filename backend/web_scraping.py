import requests
from bs4 import BeautifulSoup

# URL da página principal onde o formulário de pesquisa está
base_url = 'https://quatrorodas.abril.com.br/busca'  # Substitua pela URL real

# Termo de pesquisa
search_term = 'termo de busca'

# Payload com o nome do campo de entrada
payload = {'s': search_term}

# Enviar a solicitação GET com o termo de pesquisa
search_response = requests.get(base_url, params=payload)

# Verifique o status da resposta
if search_response.status_code == 200:
    # Parsear o HTML da resposta
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    
    # Exibir o HTML para depuração (opcional)
    print(search_soup.prettify())
    
    # Encontrar o link do artigo (ajuste o seletor conforme necessário)
    article_link = search_soup.find('a', {'class': 'article-link'})  # Ajuste a classe ou seletor
    
    if article_link:
        # Obter a URL completa do artigo
        article_url = article_link.get('href')
        if not article_url.startswith('http'):
            article_url = base_url + article_url
        
        # Enviar solicitação GET para o artigo
        article_response = requests.get(article_url)
        
        # Verifique o status da resposta
        if article_response.status_code == 200:
            # Parsear o HTML do artigo
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            
            # Encontrar o conteúdo do artigo (ajuste o seletor conforme necessário)
            article_content = article_soup.find('div', {'class': 'article-content'})  # Ajuste a classe ou seletor
            
            if article_content:
                # Exibir o conteúdo do artigo
                print(article_content.text.strip())
            else:
                print("Conteúdo do artigo não encontrado.")
        else:
            print("Não foi possível acessar o artigo.")
    else:
        print("Link do artigo não encontrado.")
else:
    print("Falha na pesquisa, status:", search_response.status_code)
