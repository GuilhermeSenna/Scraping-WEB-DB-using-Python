import requests
from functions import *
from operator import itemgetter


# Aplica o inicio simples
url = "https://www.letras.mus.br/linkin-park"
site = "https://www.letras.mus.br"
# url = "https://www.letras.mus.br/linkin-park/23091/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')


# Musicas mais ouvidas do Linin Park
dicionario = dict()
for titulo in soup.findAll('li', attrs={'class' : 'cnt-list-row -song'}):
    musica = titulo.find('a')
    print(site + musica['href'])

    page = requests.get(site + musica['href'], headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    # soup, driver = simpleinit(site + musica['href'])

    lyrics = ''
    for letra in soup.findAll('div', attrs={'class' : 'cnt-letra p402_premium'}):
        for lyric in letra.findAll('p'):
            lyrics += str(lyric).lower().replace('<p>', '').replace('</p>', '').replace('<br/>', ' ').replace('(', '').replace(')', '').replace(',', '') + ' '
    lyrics = lyrics[:len(lyrics)-1]

    palavras = lyrics.split(" ")

    for p in palavras:
        aux = 0
        if p not in dicionario:
            dicionario[p] = 1
        else:
            aux += dicionario[p] + 1
            dicionario[p] = aux

print(sorted(dicionario.items(), key=itemgetter(1), reverse=True))
