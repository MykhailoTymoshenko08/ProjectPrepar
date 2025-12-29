import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Додаємо max_tokens до налаштувань моделі
model = ChatOpenAI(
    model="meta-llama/llama-3.2-3b-instruct",
    openai_api_key=os.getenv("API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=100,  # ← ОБМЕЖЕННЯ ДОВЖИНИ!
    temperature=0.7
)

prompt = ChatPromptTemplate.from_template(
    "Ти професійний програміст. Дай коротку відповідь на питання: {topic}"
)

output_parser = StrOutputParser()
chain = prompt | model | output_parser

print("Чекаю відповідь від LangChain...")
result = chain.invoke({"topic": "Що таке рекурсія?"})

print("-" * 50)
print(f"Відповідь ({len(result)} символів):")
print(result)   