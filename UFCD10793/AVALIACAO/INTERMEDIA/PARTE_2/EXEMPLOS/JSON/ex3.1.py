'''
Converter um dicionário PYTHON para JSON
'''

import json
dados = {"nome": "João", "idade": 25, "cidade": "Lisboa"}
json_string = json.dumps(dados, indent=4)

print(json_string)