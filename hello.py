import json
def flatten_json(json_obj, delimiter='_', prefix=''):
    flattened = {}
    for key, value in json_obj.items():
        if isinstance(value, dict):
            flattened.update(flatten_json(value, delimiter, f"{prefix}{key}{delimiter}"))
        elif isinstance(value, list):
            flattened[f"{prefix}{key}"] = json.dumps(value)  # Convert list to string
        else:
            flattened[f"{prefix}{key}"] = value
    return flattened
# Example usage
input_json = {
    "id": 1,
    "info": {"name": "John", "details": {"age": 30, "city": "New York"}},
    "tags": ["developer", "blogger"]
}
flattened_json = flatten_json(input_json)
print(flattened_json)