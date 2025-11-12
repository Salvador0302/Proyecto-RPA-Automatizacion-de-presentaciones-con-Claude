# claude/claude_integration.py
"""
Plantilla mínima para llamar a Claude (ajusta según la doc/oficina).
Esto usa `requests` como ejemplo; ajusta URL/headers según la versión de API que uses.
"""

import os
import requests
import json

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")  # pon tu clave en variable de entorno
# EJEMPLO: revisa la doc real de Anthropic/Claude para la URL y formato correcto.
CLAUDE_URL = "https://api.anthropic.com/v1/complete"  

def ask_claude(prompt, max_tokens=1000):
    if not CLAUDE_API_KEY:
        raise EnvironmentError("Set CLAUDE_API_KEY env var.")
    headers = {
        "Authorization": f"Bearer {CLAUDE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-2.1",
        "prompt": prompt,
        "max_tokens": max_tokens
    }
    r = requests.post(CLAUDE_URL, headers=headers, json=payload)
    r.raise_for_status()
    return r.json()

def prompt_for_presentation(topic, slides=5):
    """
    Prompt que pide a Claude devolver JSON con la estructura de slides.
    Copia y pega exactamente en la API.
    """
    return f"""
Genera una presentación sobre "{topic}" con {slides} slides en formato JSON.
Cada slide debe ser un objeto con "title", "bullets" (lista) y opcional "image" (URL).
Devuelve **solo** JSON válido: [{"{"} "title": "...", "bullets": ["..."] {"}"}].
No expliques nada fuera del JSON.
"""

if __name__ == "__main__":
    p = prompt_for_presentation("RPA con Python y Claude", slides=5)
    print("Prompt para Claude:\n")
    print(p)
    # Si quieres llamar a la API:
    # res = ask_claude(p)
    # print(json.dumps(res, indent=2))
