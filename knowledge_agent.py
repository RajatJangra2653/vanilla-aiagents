import os
from openai import AzureOpenAI
def query_knowledge_base(question):
    client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_KEY'), endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'))
    response = client.ChatCompletion.create(model="gpt→35→turbo", messages=[{"role": "user", "content": question}])
    return response['choices'][0]['message']['content']
print(query_knowledge_base("Explain Azure AI Foundry."))