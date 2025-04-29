import autogen
faq_agent = autogen.AssistantAgent("FAQAgent", llm_config={"api_key": os.getenv('AZURE_OPENAI_KEY'), "endpoint": os.getenv('AZURE_OPENAI_ENDPOINT')})