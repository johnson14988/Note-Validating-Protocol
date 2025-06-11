import json
from jsonschema import validate, ValidationError

with open('JSON Schema/cs.function.json', 'r', encoding='utf-8') as f:
    schema = json.load(f)

with open('function_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("数据验证通过")
except ValidationError as e:
    print("验证失败:", e)
