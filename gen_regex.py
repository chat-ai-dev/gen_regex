from langchain.prompts import ChatPromptTemplate

from mad_hatter.decorators import tool


@tool
def generate_regex(regex_description: str, bot):
	"""Replies to "regex xxx". Input is the description of the Regular Expression (regex), which start with 'regex '."""

	human_message_prompt = f"""You are an intelligent AI that passes the Turing test specialized in Regular Expression (regex) generation.
Write a Regular Expression (regex) to match the following sentence:
{regex_description}
Just answer with a regex without explanation
"""
	chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])
	message = bot.llm(chat_prompt.format_prompt(regex_description=regex_description).to_messages())

	return message.content
