from bs4 import BeautifulSoup
import requests
from time import sleep

# Usar Chrome
# driver = webdriver.Chrome(chrome())

# Stephen King
# driver.get("https://www.amazon.com.br/s?k=stephen+king&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

# Agatha Christie
# driver.get("https://www.amazon.com.br/s?k=agatha+christie&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
page = requests.get("https://www.amazon.com.br/s?k=distopia&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2", headers=headers)
page.raise_for_status()

print(page.status_code)


soup = BeautifulSoup(page.text, 'html.parser')

text = ""

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
                text += f'{nome.string} - Nota nao disponivel - Preco nao disponivel \n'
                # print(f'{nome.string} - Nota nao disponivel - Preco nao disponivel')
            else:
                text += f'{nome.string} - Nota nao disponivel - Preco {preco.string} \n'
                # print(f'{nome.string} - Nota nao disponivel - Preco {preco.string}')
        else:
            try:
                preco.string
            except AttributeError:
                text += f'{nome.string} - Nota: {nota.string} - Preco nao disponivel \n'
                # print(f'{nome.string} - Nota: {nota.string} - Preco nao disponivel')
            else:
                text += f'{nome.string} - Nota: {nota.string} - Preco {preco.string} \n'
                # print(f'{nome.string} - Nota: {nota.string} - Preco {preco.string}')

print(text)