import json

dic = {"name": "yuki", "numbers": [1, 2, 3], "is_morning": True}

# dump
with open("test.json", "w") as f:
    json.dump(dic, f, indent=2)

# dumps
json_str = json.dumps(dic)
print(f"dumps: {json_str}")
