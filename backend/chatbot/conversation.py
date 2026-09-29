def companion_reply(patient_name: str, message: str):
    message = message.lower()

    if any(word in message for word in ["scared", "anxious", "worried"]):
        return (
            f"I'm here with you, {patient_name}. "
            "That sounds stressful. Can you tell me whether you're feeling physically unwell, "
            "or is it mainly the anxiety that's bothering you?"
        )

    if any(word in message for word in ["chest", "pain"]):
        return (
            "Thanks for telling me. I'd like to understand this better. "
            "Is the discomfort mild, or does it feel severe or crushing?"
        )

    return (
        f"Thanks for checking in, {patient_name}. "
        "I'm listening. Tell me a little more about how you're feeling."
    )