from extrai.extraiDoOlx import extractOlx
from time import sleep
import json

while True:
    URL = input("Digite a URL de entrada: ")
    apartamentos = extractOlx(URL)
    print(json.dumps(apartamentos, indent=4, ensure_ascii=False))