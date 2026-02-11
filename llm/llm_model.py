import ollama

def ollama_llm(prompt: str, model: str = "llama3.2"):
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={
            "temperature": 0,
            "num_ctx": 4096
        }
    )
    return response["response"].strip()
