import json

def get_scheme_details(scheme_name):
    with open("data/schemes.json", "r", encoding="utf-8") as f:
        schemes = json.load(f)
    
    return schemes.get(scheme_name, "వివరాలు లభించలేదు")
