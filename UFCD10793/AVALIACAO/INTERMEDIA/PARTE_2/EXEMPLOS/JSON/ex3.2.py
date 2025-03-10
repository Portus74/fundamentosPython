'''
Converter JSON para dicionário PYTHON
'''

import json
json_string = '{"nome": "João", "idade": 25, "cidade": "Lisboa"}'
dados = json.loads(json_string)

print(dados["nome"])