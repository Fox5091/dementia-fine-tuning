import openai

def GPT_response(message):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        model="ft:babbage-002:personal::9ZE6fYq4",  # 使用您的微调模型 ID
        prompt=message,
        max_tokens=150,
        temperature=0.7,
        stop=["\n", " User:", " Assistant:"]
    )
    return response.choices[0].text.strip()
