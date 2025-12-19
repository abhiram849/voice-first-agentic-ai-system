import re
from voice.stt import listen_telugu
from voice.tts import speak_telugu
from memory.memory_store import MemoryStore
from agent.planner import planner
from agent.executor import executor
from agent.evaluator import evaluate

print("APP STARTED")

memory = MemoryStore()

speak_telugu("ప్రభుత్వ పథకాల సహాయకుడికి స్వాగతం")

while True:
    user_input = listen_telugu()

    error = evaluate(user_input)
    if error:
        speak_telugu(error)
        continue

    # --------- ROBUST INCOME HANDLING (FIXED) ----------
    if "ఆదాయం" in user_input:
        numbers = re.findall(r"\d+", user_input)
        if numbers:
            memory.update("income", int(numbers[0]))
        else:
            speak_telugu("దయచేసి మీ ఆదాయాన్ని అంకెలలో చెప్పండి. ఉదాహరణకు 150000")
            continue

    # --------- OTHER USER DETAILS ----------
    elif "పురుషుడు" in user_input:
        memory.update("gender", "male")

    elif "మహిళ" in user_input:
        memory.update("gender", "female")

    elif "రైతు" in user_input:
        memory.update("job", "farmer")

    # --------- AGENTIC FLOW ----------
    plan = planner(user_input, memory)
    responses = executor(plan, memory)

    for r in responses:
        speak_telugu(r)
