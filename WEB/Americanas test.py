from bs4 import BeautifulSoup
import requests
from random import choice
from time import sleep

def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0', }
    # proxies_list = ['102.129.249.120:3128', '88.198.24.108:8080', '	159.8.114.34:25', '	91.205.174.26:80']
    # proxies = {'https': choice(proxies_list)}

    page = requests.get(url, headers=headers)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.prettify())
    # print(soup.prettify())
    preco_atual = soup.find('div', attrs={
        'class': 'src__BestPrice-lo2vta-5 bFIChl priceSales'})

    print(preco_atual.contents[2])

    div_vendido = soup.find('div', attrs={'class':'offers-box__Wrapper-sc-12ywm4y-0 ekBHLZ'})
    vendido = div_vendido.find('p')
    print(vendido.contents[1])

    foto = soup.findAll('img', attrs={'class':'src__Image-xr9q25-0 jLfQuZ'})
    print(foto)
    # foto = picture_foto.find('img')
    # print(foto)


    # preco_antigo = soup.find('span', attrs={'class': 'a-color-secondary a-text-strike'})
    #
    # sem_estoque = soup.find('a', attrs={'id': 'buybox-see-all-buying-choices-announce'})
    # vendido_amazon = soup.find('div', attrs={'id': 'merchant-info'})
    #
    # info = dict()
    #
    # titulo = soup.find('span', attrs={'id': 'productTitle'})
    # # divfoto = soup.find('div', attrs={'class': 'a-column a-span3 a-spacing-micro imageThumb thumb'})
    # # foto = divfoto.find('img')
    # foto = soup.find('img', attrs={'id': 'imgBlkFront'})
    # categoria = soup.find('a', attrs={'class': 'a-link-normal a-color-tertiary'})
    # codigo = soup.find('input', attrs={'id': 'ASIN'})
    #
    # try:
    #     strfoto = str(foto['data-a-dynamic-image'])
    # except TypeError:
    #     photo = ''
    # else:
    #     print(strfoto[strfoto.find('"')+1: (strfoto[strfoto.find('"')+1:]).find('"')+2])
    #     photo = strfoto[strfoto.find('"')+1: (strfoto[strfoto.find('"')+1:]).find('"')+2]
    #
    #
    # if sem_estoque:
    #     return 'O produto não tem estoque disponível.'
    # else:
    #     try:
    #         vendido_amazon.contents[0]
    #     except AttributeError:
    #         return (
    #             'Erro, talvez você esteja pedindo a requisição rápido demais, aguardando alguns segundos para solicitar'
    #             ' novamente!! \n Por favor, tente novamente!')
    #
    #     else:
    #         if vendido_amazon.contents[0] is None:
    #             return (
    #                 'Erro, talvez você esteja pedindo a requisição rápido demais, aguardando alguns segundos para solicitar'
    #                 ' novamente!! \n Por favor, tente novamente!')
    #
    #         if 'Enviado e vendido por Amazon.com.br.' in str(vendido_amazon.contents[0]):
    #             info['titulo'] = titulo.string.strip()
    #             info['foto'] = photo
    #             info['categoria'] = categoria.string.strip()
    #             info['codigo'] = codigo.attrs['value']
    #             info['preco'] = preco_atual.contents[0]
    #             return info
    #         else:
    #             return 'Vendido por terceiros.'




print(main('https://www.americanas.com.br/produto/5640514'))