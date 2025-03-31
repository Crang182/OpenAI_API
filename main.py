#Importe der librarys
import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

#Datenbank zur Protokollierung der Complition- und Prompt Tokens
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("token_usage.db")
cursor = conn.cursor()

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