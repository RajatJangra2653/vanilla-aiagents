import autogen
manager = autogen.GroupChatManager()
group_chat = autogen.GroupChat(agents=[faq_agent, doc_agent, summarization_agent], messages=[])
manager.manage(group_chat)