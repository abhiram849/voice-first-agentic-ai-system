def check_eligibility(user):
    schemes = []

    if user.get("income", 0) < 200000:
        schemes.append("ఆయుష్మాన్ భారత్")
    
    if user.get("gender") == "female":
        schemes.append("మహిళా శక్తి పథకం")

    if user.get("job") == "farmer":
        schemes.append("రైతు భరోసా")

    return schemes
