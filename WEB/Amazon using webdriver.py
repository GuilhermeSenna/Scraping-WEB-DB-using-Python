from selenium import webdriver
from bs4 import BeautifulSoup
from functions import chrome, site, pdf
import requests
import pdfkit

# Usar Chrome
driver = webdriver.Chrome(chrome())

# Stephen King
# driver.get("https://www.amazon.com.br/s?k=stephen+king&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

#Agatha Christie
# driver.get("https://www.amazon.com.br/s?k=agatha+christie&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

driver.get("https://www.amazon.com.br/s?k=distopia&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for produto_descricao in soup.findAll('div', attrs={'data-component-type': 's-search-result'}):
    for produto_detalhes in produto_descricao.findAll('div', attrs={
        'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col '
                 'sg-col-28-of-36 sg-col-20-of-28'}):
        nome = produto_descricao.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
        nota = produto_descricao.find('span', attrs={'class': 'a-icon-alt'})
        preco = produto_descricao.find('span', attrs={'class': 'a-offscreen'})

        try:
            nota.string
        except AttributeError:
            try:
                preco.string
            except AttributeError:
                print(f'{nome.string} - Nota nao disponivel - Preco nao disponivel')
            else:
                print(f'{nome.string} - Nota nao disponivel - Preco {preco.string}')
        else:
            try:
                preco.string
            except AttributeError:
                print(f'{nome.string} - Nota: {nota.string} - Preco nao disponivel')
            else:
                print(f'{nome.string} - Nota: {nota.string} - Preco {preco.string}')

driver.close()
