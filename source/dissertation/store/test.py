dict = {
    "key1": "value",
    "key2": {
        "subkey1": "value",
        "subkey2": "value"
    }
}

print dict

print dict.get("key4", {}).get("subkey1", "nothing1")