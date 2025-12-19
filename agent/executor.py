from tools.eligibility_engine import check_eligibility
from tools.scheme_api import get_scheme_details

def executor(plan, memory):
    responses = []

    for step in plan:
        if step == "ASK_INCOME":
            responses.append("మీ వార్షిక ఆదాయం ఎంత?")
        elif step == "ASK_GENDER":
            responses.append("మీ లింగం ఏమిటి?")
        elif step == "ASK_JOB":
            responses.append("మీ వృత్తి ఏమిటి?")
        elif step == "CHECK_ELIGIBILITY":
            schemes = check_eligibility(memory.all())
            for s in schemes:
                responses.append(get_scheme_details(s))

    return responses
