import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import paramiko

# Load environment variables
load_dotenv()

# Remote connection settings
REMOTE_HOST = os.getenv('REMOTE_HOST')
REMOTE_USER = os.getenv('REMOTE_USER')
SSH_PORT = int(os.getenv('SSH_PORT', '22'))
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL')

# Ollama configuration
config_list = [{
    'model': 'ollama/codellama',
    'base_url': OLLAMA_BASE_URL,
    'api_key': ''  # Ollama doesn't require API key
}]

# Create specialized agents
product_owner = AssistantAgent(
    name="product_owner",
    system_message="You are a Product Owner. You define requirements, acceptance criteria, and ensure the project aligns with business goals.",
    llm_config={"config_list": config_list}
)

architect = AssistantAgent(
    name="architect",
    system_message="You are a Software Architect. You design system architecture and make technical decisions.",
    llm_config={"config_list": config_list}
)

programmer = AssistantAgent(
    name="programmer",
    system_message="You are a Senior Programmer. You write code, implement features, and handle technical implementation.",
    llm_config={"config_list": config_list}
)

devops = AssistantAgent(
    name="devops",
    system_message="You are a DevOps Engineer. You handle deployment, infrastructure, and automation scripts.",
    llm_config={"config_list": config_list}
)

qa_engineer = AssistantAgent(
    name="qa_engineer",
    system_message="You are a QA Engineer. You create test plans and ensure code quality.",
    llm_config={"config_list": config_list}
)

# Create user proxy for task execution
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "workspace",
        "use_docker": False
    }
)

# Set up group chat
groupchat = GroupChat(
    agents=[user_proxy, product_owner, architect, programmer, devops, qa_engineer],
    messages=[],
    max_round=50
)

manager = GroupChatManager(groupchat=groupchat)

if __name__ == "__main__":
    # Start the conversation with a project initialization
    user_proxy.initiate_chat(
        manager,
        message="Let's start the development project. First, let's define the requirements and architecture."
    ) 