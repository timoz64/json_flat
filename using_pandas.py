import pandas as pd

# # Example JSON data with nested arrays
# data = {
#     "id": 1,
#     "name": "John Doe",
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown"
#     },
#     "phones": [
#         {"type": "home", "number": "123-456-7890"},
#         {"type": "work", "number": "987-654-3210"}
#     ]
# }

# # Flatten JSON data, including nested arrays
# df = pd.json_normalize(data, 'phones', ['id', 'name', ['address', 'street'], ['address', 'city']])
# print(df)


# Example JSON data with deeper nested structure
data = [
    {
        "id": 1,
        "name": "John Doe",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "geo": {
                "lat": "40.7128",
                "long": "74.0060"
            }
        },
        "phones": [
            {"type": "home", "number": "123-456-7890"},
            {"type": "work", "number": "987-654-3210"}
        ]
    },
    {
        "id": 1,
        "name": "John Doe",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "geo": {
                "lat": "40.7128",
                "long": "74.0060"
            }
        },
        "phones": [
            {"type": "home", "number": "999-456-0000"}
        ]
    }
]

# Flatten JSON data, including deeper nested fields
df = pd.json_normalize(data, 'phones', ['id', 'name', ['address', 'street'], ['address', 'city'], ['address', 'geo', 'lat'], ['address', 'geo', 'long']])
print(df)