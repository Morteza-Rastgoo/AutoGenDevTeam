from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Configure the OpenAI API key and model settings
config_list = [
    {
        'model': 'gpt-4',
        'api_key': 'your-api-key-here'
    }
]

# Create an assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list
    }
)

# Create a user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",  # Don't ask for human input
    max_consecutive_auto_reply=10
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a Python function to calculate the fibonacci sequence"
) 