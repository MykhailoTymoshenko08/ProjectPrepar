#input data

#Response from the first model (Llama 3)
response_1 = {
    "model": "meta-llama/llama-3-8b",
    "usage": {"total_tokens": 150},
    "choices": [
        {"message": {"content": "Привіт! Я Llama. Твій код працює чудово."}}
    ]
}

#Response from the second model (Gemini)
response_2 = {
    "model": "google/gemini-pro",
    "usage": {"total_tokens": 125},
    "choices": [
        {"message": {"content": "Вітаю! Я Gemini. Ти стаєш справжнім розробником."}}
    ]
}

text1 = response_1["choices"][0]["message"]["content"]
text2 = response_2["choices"][0]["message"]["content"]
token1 = response_1["usage"]["total_tokens"]
token2 = response_2["usage"]["total_tokens"]
print(response_1["model"], text1)
print(response_2["model"], text2)
print("The token's sum: ", token1+token2)

print(response_1["model"], "is more economy") if token1<token2 else print(response_2["model"], "is more economy")

del text1
del text2