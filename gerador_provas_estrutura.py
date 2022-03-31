import random
import csv
def criarArquivos():
    estados = 'Acre\nAlagoas\nAmapá\nAmazonas\nBahia\nCeará\nDistrito Federal\nEspírito Santo\nGoiás\nMaranhão\nMato Grosso\nMato Grosso do Sul\nMinas Gerais\nPará\nParaíba\nParaná\nPernambuco\nPiauí\nRio de Janeiro\nRio Grande do Norte\nRio Grande do Sul\nRondônia\nRoraima\nSanta Catarina\nSão Paulo\nSergipe\nTocantins'
    capitais = 'Rio Branco\nMaceió\nMacapá\nManaus\nSalvador\nFortaleza\nBrasília\nVitória\nGoiânia\nSão Luís\nCuiabá\nCampo Grande\nBelo Horizonte\nBelém\nJoão Pessoa\nCuritiba\nRecife\nTeresina\nRio de Janeiro\nNatal\nPorto Alegre\nPorto Velho\nBoa Vista\nFlorianópolis\nSão Paulo\nAracaju\nPalmas'
    arquivo = open("estados.txt", "a")
    arquivo.write(estados)
    arquivo.close()
    arquivo = open("capitais.txt", "a")
    arquivo.write(capitais)
    arquivo.close()
criarArquivos()