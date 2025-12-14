from typing import List, Dict
from openai import OpenAI


class AIAssistant:
    """
    A class that wraps AI assistant behaviour.
    This separates the AI logic from the Streamlit UI.
    """

    def __init__(self, system_prompt: str):
        # Create OpenAI client (you can also pass API key here if needed)
        self._client = OpenAI()

        # Store the system prompt (AI behaviour instructions)
        self._system_prompt = system_prompt

        # Conversation history (in the format OpenAI expects)
        self._history: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def send_message(self, user_message: str) -> str:
        """
        Send a message to the AI and return its reply.
        History is stored inside the class so Streamlit UI stays clean.
        """

        # Add user message to history
        self._history.append({"role": "user", "content": user_message})

        # Call the OpenAI Chat API
        response = self._client.chat.completions.create(
            model="gpt-4o",
            messages=self._history
        )

        # Extract assistant response text
        reply = response.choices[0].message["content"]

        # Save reply in history
        self._history.append({"role": "assistant", "content": reply})

        return reply

    def clear_history(self):
        """Reset conversation history (except system prompt)."""
        self._history = [
            {"role": "system", "content": self._system_prompt}
        ]
