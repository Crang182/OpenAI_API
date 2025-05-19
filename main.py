#Importe der librarys
import os
import re

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

#Datenbank zur Protokollierung der Complition- und Prompt Tokens
import sqlite3

#Datenbank zur Protokollierung der Complition- und Prompt Tokens
import sqlite3

# Api key von .env ziehen und testen
#client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#print("OPENAI_API_KEY")

def save_token_usage(response, vendor="OpenAI"):
    usage = response.usage
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    model_used = response.model

    conn = sqlite3.connect("token_usage.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO token_usage (prompt_tokens, completion_tokens, model, vendor)
    VALUES (?, ?, ?, ?)
    """, (prompt_tokens, completion_tokens, model_used, vendor))

    conn.commit()
    conn.close()

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("token_usage.db")
cursor = conn.cursor()

#Inner thoughts // Utterance extrahieren
import re

string_0 = "inner_thoughts:  asdf   utterance: something"
match = re.search(r"inner_thoughts:\s*(.*?)\s*utterance:", string_0)

if match:
    print(match.group(1).strip())  # Ausgabe: asdf


# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS token_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    prompt_tokens INTEGER,
    completion_tokens INTEGER,
    model TEXT,
    vendor TEXT
)
""")

# Eintrag hinzufügen
cursor.execute("""
INSERT INTO token_usage (prompt_tokens, completion_tokens, model, vendor)
VALUES (?, ?, ?, ?)
""", (42, 58, "gpt-4o", "OpenAI"))

conn.commit()
conn.close()

#Parameter festlegen
QUESTION = "What is the capitol of france?"
SYSTEM_PROMPT = "You are a helpful assistant that can answer questions, but always lie!"

MODEL = "gpt-4o-mini"

## MAIN
# .env laden

load_dotenv("C:/Users/Anwender/Desktop/Uni/test/.env", override=True)
load_dotenv("C:\\Users\\Anwender\\Desktop\\Uni\\OpenAI_API-main\\.env", override=True)

#initiate openai client

api_key =os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

print(api_key)

# Messages definieren
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": QUESTION}
]

print(messages)

print("Done.")

response = client.chat.completions.create(model=MODEL, messages=messages)

print()

response.choices[0].message.content
"""
client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("OPENAI_API_KEY")"
"""
=======
# Gemeinsame Instruktion für Monolog + Äußerung
common_instruction = (
    "Ich will, dass du dir zunächst Gedanken machst, was du sagen möchtest, um dein Ziel zu erreichen. "
    "Schreibe dazu 'Innere Gedanken:', dann deine Gedanken in drei Sätzen. Danach 'Aussage:', gefolgt von deiner eigentlichen Aussage in drei Sätzen. "
    "Antworte bitte in einer Zeile ohne Zeilenumbrüche."
)

# Zwei Charaktere
system_prompt_0 = "Du bist ein idealistischer Student, voller Enthusiasmus. " + common_instruction
system_prompt_1 = "Du bist ein pragmatischer Studienberater. " + common_instruction

kickoff = "Wie bleibst du während des Studiums motiviert?"

messages_0 = [
    {"role": "system", "content": system_prompt_0},
    {"role": "user", "content": kickoff}
]

messages_1 = [
    {"role": "system", "content": system_prompt_1}
]

# Starte Schleife
for _ in range(5):
    # GPT-Antwort von Student
    res_0 = client.chat.completions.create(model=MODEL, messages=messages_0)
    content_0 = res_0.choices[0].message.content
    print("🎓 Student antwortet:", content_0)

    # Token speichern
    save_token_usage(res_0)

    match_0 = re.search(r"Innere Gedanken:\s*(.*?)\s*Aussage:\s*(.*)", content_0, re.DOTALL)
    result_0 = match_0.group(2).strip() if match_0 else "⚠️ Kein gültiger Output von Student"
    messages_0.append({"role": "assistant", "content": content_0})
    messages_1.append({"role": "user", "content": result_0})

    # GPT-Antwort von Studienberater
    res_1 = client.chat.completions.create(model=MODEL, messages=messages_1)
    content_1 = res_1.choices[0].message.content
    print("🧑‍💼 Berater antwortet:", content_1)

    # Token speichern
    save_token_usage(res_1)

    match_1 = re.search(r"Innere Gedanken:\s*(.*?)\s*Aussage:\s*(.*)", content_1, re.DOTALL)
    result_1 = match_1.group(2).strip() if match_1 else "⚠️ Kein gültiger Output vom Berater"
    messages_1.append({"role": "assistant", "content": content_1})
    messages_0.append({"role": "user", "content": result_1})




#Nächstes Mal: chatgpt.com/share/67f40bca-c6b4-8008-be73-eded6d31edc0
