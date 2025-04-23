import json
import requests


def similar_words_finder(word: str, maxLength: int) -> list:
    prompt = f"""
return an array of words no greater than {maxLength} letters each related to the word '{word}'

your response should only be a single array:
"""
    try:
        words = eval(message_ai(prompt))
        return words
    except SyntaxError as e:
        print(f"Invalid syntax: {e}")

    return []


def clue_for_word(word: str) -> str:
    # TODO update to stop AI from giving me a long response
    prompt = f"""Return a small clue for the word '{word}' that can be used in a crossword puzzle"""
    try:
        words = message_ai(prompt)
        return words
    except SyntaxError as e:
        print(f"Invalid syntax: {e}")

    return ""


def message_ai(prompt: str):
    url = "http://localhost:11434/api/generate"
    data = {"prompt": prompt, "model": "llama3.2", "stream": False}

    # Optional: If authentication is needed
    headers = {
        "Content-Type": "application/json",
    }

    # Make the POST request to the LLM
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response
    if response.status_code == 200:
        # print("Response from LLM:", response.text)
        data = response.json()
        print("Response from LLM:", data["response"])
        return data["response"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
