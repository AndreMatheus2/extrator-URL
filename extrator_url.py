import re
class ExtratoURL:
    def __init__(self, url):
        self.url = self.sanitizaUrl(url)
        self.validaUrl()

    def sanitizaUrl(self, url):
        return url.strip()

    def validaUrl(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def getUrlBase(self):
        indiceInterrogacao = self.url.find('?')
        url_base = self.url[:indiceInterrogacao]
        return url_base

    def getUrlParametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def getValorParametro(self, parametroBusca):
        indiceParametro = self.getUrlParametro().find(parametroBusca)
        indiceValor = indiceParametro + len(parametroBusca) + 1
        indiceEComercial = self.getUrlParametro().find('&', indiceValor)
        if indiceEComercial == -1:
            valor = self.getUrlParametro()[indiceValor:]
        else:
            valor = self.getUrlParametro()[indiceValor:indiceEComercial]
        return valor


url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extratorUrl = ExtratoURL(url)
valorQuantidade = extratorUrl.getValorParametro('quantidade')
print(valorQuantidade)