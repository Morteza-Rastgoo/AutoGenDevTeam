import autogen
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import os

# Configure remote Ollama settings
OLLAMA_BASE_URL = f"http://10.251.165.183:11434"
MODEL_NAME = "codellama"

# Configure the agents with Ollama
config_list = [
    {
        "base_url": OLLAMA_BASE_URL,
        "api_key": "ollama",  # Not needed for Ollama but required by AutoGen
        "model": MODEL_NAME,
    }
]

# Basic configuration for all agents
llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
    "request_timeout": 120,
}

# Create the development team agents
product_owner = autogen.AssistantAgent(
    name="ProductOwner",
    system_message="You are a Product Owner. You define requirements, prioritize features, and ensure the team delivers business value. You communicate in user stories and acceptance criteria.",
    llm_config=llm_config,
)

tech_lead = autogen.AssistantAgent(
    name="TechLead",
    system_message="You are a Technical Lead. You make architectural decisions, review technical approaches, and ensure code quality. You break down tasks and provide technical guidance.",
    llm_config=llm_config,
)

programmer = autogen.AssistantAgent(
    name="Programmer",
    system_message="You are a Senior Programmer. You write clean, efficient code following best practices. You implement features based on requirements and technical specifications.",
    llm_config=llm_config,
)

qa_engineer = autogen.AssistantAgent(
    name="QAEngineer",
    system_message="You are a QA Engineer. You write and review test cases, identify potential issues, and ensure software quality. You think about edge cases and user scenarios.",
    llm_config=llm_config,
)

# Create a user proxy that can execute code
user_proxy = RetrieveUserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    system_message="Execute code and provide feedback. Handle file operations and development tasks.",
    code_execution_config={
        "work_dir": "project_workspace",
        "use_docker": False,
    },
)

# Create the group chat for the team
groupchat = autogen.GroupChat(
    agents=[user_proxy, product_owner, tech_lead, programmer, qa_engineer],
    messages=[],
    max_round=50
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
)

# Create project workspace directory
if not os.path.exists("project_workspace"):
    os.makedirs("project_workspace")

# Start the development process
user_proxy.initiate_chat(
    manager,
    message="""
    Let's develop a FastAPI-based REST API for a task management system. 
    Requirements:
    1. CRUD operations for tasks
    2. User authentication
    3. Task categories and priorities
    4. Due date management
    
    Start by setting up the project structure and implementing the core features.
    """
) 