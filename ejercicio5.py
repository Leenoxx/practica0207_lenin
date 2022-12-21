# Escribir un programa que abra el fichero con información
# sobre el PIB per cápita de los países de la Unión
# Europea,pregunte por las iniciales de un país y muestre el PIB
# per cápita de ese país de todos los años disponibles.
import urllib.request


def abrir_fichero_pib(url, letra):
    file = urllib.request.urlopen(url)
    diccionario = {}
    for line in file:
        decoded_line = line.decode("utf-8")
        lista = decoded_line.split()
        inicial = lista[0].split(",")
        lista.pop(0)
        diccionario[inicial[2]] = lista
    return diccionario.get(letra, "Valor no asociado!")


inicial_pais = input("Escribe las iniciales del país para ver su PIB per cápita: ")
mayuscula = inicial_pais.upper()
fichero = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/" \
          "BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
print(abrir_fichero_pib(fichero, mayuscula))
