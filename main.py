url = 'httpa://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

url = url.strip()

if url == '':
    raise ValueError('URL vazia')

indiceInterrogacao = url.find('?')
urlBase = url[:indiceInterrogacao]
print(urlBase)

urlParametro = url[indiceInterrogacao+1:]
print(urlParametro)

parametroBusca = 'moedaDestino'
indiceParametro = urlParametro.find(parametroBusca)
indiceValor = indiceParametro + len(parametroBusca) + 1
indiceEComercial = urlParametro.find('&', indiceValor)
if indiceEComercial == -1:
    valor = urlParametro[indiceValor:]
else:
    valor = urlParametro[indiceValor:indiceEComercial]
print(valor)