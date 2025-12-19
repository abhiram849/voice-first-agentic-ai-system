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

    if "ఆదాయం" in user_input:
        memory.update("income", int(user_input.split()[-1]))
    elif "పురుషుడు" in user_input:
        memory.update("gender", "male")
    elif "మహిళ" in user_input:
        memory.update("gender", "female")
    elif "రైతు" in user_input:
        memory.update("job", "farmer")

    plan = planner(user_input, memory)
    responses = executor(plan, memory)

    for r in responses:
        speak_telugu(r)
