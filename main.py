import autogen
from faq_agent import faq_agent
from doc_agent import doc_agent

user_proxy = autogen.UserProxyAgent("user", human_input_mode="TERMINATE", llm_config={})
user_proxy.initiate_chat(faq_agent, message="What are the key features of Azure OpenAI?")