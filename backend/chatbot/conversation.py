from typing import Dict, List


# Temporary in-memory conversation storage.
# We'll replace this with a database later.
conversation_history: Dict[str, List[dict]] = {}


def save_message(patient_id: str, role: str, message: str):
    """Save one message to the patient's conversation history."""

    if patient_id not in conversation_history:
        conversation_history[patient_id] = []

    conversation_history[patient_id].append({
        "role": role,
        "message": message
    })


def get_history(patient_id: str):
    """Return the conversation history for a patient."""

    return conversation_history.get(patient_id, [])


def generate_basic_reply(patient_name: str, message: str):
    """
    Temporary companion logic.
    This will eventually be replaced/enhanced by the LLM.
    """

    text = message.lower()

    if any(word in text for word in [
        "scared",
        "scary",
        "anxious",
        "anxiety",
        "worried",
        "nervous"
    ]):
        return (
            f"I'm here with you, {patient_name}. "
            "It sounds like you're feeling worried. "
            "Can you tell me a little more about what's making you feel this way?"
        )

    if any(word in text for word in [
        "chest pain",
        "chest hurts",
        "chest discomfort"
    ]):
        return (
            "Thank you for telling me. "
            "Can you tell me whether the discomfort is mild or severe, "
            "and whether you're experiencing anything else right now?"
        )

    if any(word in text for word in [
        "dizzy",
        "dizziness",
        "lightheaded"
    ]):
        return (
            "I'm sorry you're feeling that way. "
            "Are you sitting or resting somewhere safely right now?"
        )

    if any(word in text for word in [
        "fine",
        "okay",
        "good"
    ]):
        return (
            f"That's good to hear, {patient_name}. "
            "I'm still here if anything changes or you want to talk."
        )

    return (
        f"Thanks for telling me, {patient_name}. "
        "I'm listening. Can you tell me a little more about how you're feeling?"
    )