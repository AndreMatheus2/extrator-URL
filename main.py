url = 'httpa://bytebank.com/cambio?moedaOrigem=real'

indiceInterrogacao = url.find('?')
urlBase = url[:indiceInterrogacao]
print(urlBase)

urlParametro = url[indiceInterrogacao+1:]
print(urlParametro)

parametroBusca = 'moedaOrigem'
indiceParametro = urlParametro.find(parametroBusca)
indiceValor = indiceParametro + len(parametroBusca) + 1
valor = urlParametro[indiceValor:]
print(valor)