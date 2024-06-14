import openai
import os

# 从环境变量中读取 API 密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

# 确保 API 密钥已正确设置
if openai.api_key is None:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# 使用正确的模型 ID（格式为 ft-XXXXX）
fine_tuned_model_id = 'ft:babbage-002:personal::9ZE6fYq4'  # 替換為實際的微調模型 ID

# 定義生成文本的函數
def generate_text(prompt, model_id):
    response = openai.Completion.create(
        model=model_id,
        prompt=prompt,
        max_tokens=150,  # 可以根據需要調整
        temperature=0.7,  # 控制輸出的隨機性
        stop=["\n", " User:", " Assistant:"]
    )
    return response.choices[0].text.strip()

# 初始提示
prompt = "你是一個樂於助人的助手。今天我可以怎麼幫助你？\nUser: 你好!\nAssistant: 你好！請問有什麼我可以幫忙的嗎？"

# 進行對話
while True:
    user_input = input("User: ")
    prompt += "\nUser: " + user_input + "\nAssistant:"
    response_content = generate_text(prompt, fine_tuned_model_id)
    prompt += " " + response_content
    print("Assistant:", response_content)
