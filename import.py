import yaml, json

with open("schema_config.yaml", "r", encoding="utf-8") as file:

    data = yaml.safe_load(file)
    print(data)
    with open('example2.txt', 'w') as file2:
       file2.write(json.dumps(data))

with open("biolink_model.yaml", "r", encoding="utf-8") as file:

    data = yaml.safe_load(file)
    print(data)
    with open('example2.txt', 'w') as file2:
       file2.write(json.dumps(data))
