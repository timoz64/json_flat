from flatten_json import flatten


input_json = {
    "results": {
    "vouchers": [
        {
    "id": 1,
    "info": {"name": "John", "details": {"age": 30, "city": "New York"}},
    "tags": ["developer", "blogger"]
},
                {
    "id": 2,
    "info": {"name": "Timo", "details": {"age": 60, "city": "Helsinki"}},
    "tags": ["dataengineer", "consult"]
},
     ]
    }
    }
# print(input_json["results"]["vouchers"])
# for voucher in input_json["results"]["vouchers"]:
#     print(voucher)

# flatted = flatten(input_json)
flatted = flatten(input_json, root_keys_to_ignore={'tags'})

print(flatted)