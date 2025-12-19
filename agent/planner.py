def planner(user_input, memory):
    plan = []

    if not memory.get("income"):
        plan.append("ASK_INCOME")

    if not memory.get("gender"):
        plan.append("ASK_GENDER")

    if not memory.get("job"):
        plan.append("ASK_JOB")

    if not plan:
        plan.append("CHECK_ELIGIBILITY")

    return plan
