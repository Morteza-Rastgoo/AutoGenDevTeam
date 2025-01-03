from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Configure the agents
config_list = [
    {
        'model': 'gpt-4',
        'api_key': 'your-api-key-here'
    }
]

# Create a coding assistant
coder = AssistantAgent(
    name="coder",
    llm_config={
        "config_list": config_list
    },
    system_message="You are a Python expert. Write code to solve problems."
)

# Create a code reviewer
reviewer = AssistantAgent(
    name="reviewer",
    llm_config={
        "config_list": config_list
    },
    system_message="You are a code reviewer. Review code for bugs and improvements."
)

# Create a user proxy
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10
)

# Start a group chat
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, reviewer],
    messages=[],
    max_round=12
)

manager = autogen.GroupChatManager(groupchat=groupchat)

# Initiate the chat
user_proxy.initiate_chat(
    manager,
    message="Create a web scraper using Beautiful Soup"
) 