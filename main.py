import autogen

config_list_model1 = [
    {"model": "ollama/llama2", "base_url": "http://0.0.0.0:8000", "api_key": "NULL"}
]

config_list_model2 = [
    {"model": "ollama/codellama", "base_url": "http://0.0.0.0:41432", "api_key": "NULL"}
]

llm_config_model1 = {
    "config_list": config_list_model1,
}

llm_config_model2 = {
    "config_list": config_list_model2,
}

coder = autogen.AssistantAgent(name="Coder", llm_config=llm_config_model2)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_model1,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task = """
Please write a python script to output numbers 1 to 100 and then the user_proxy agent should run the script. Print success in the end.
"""

user_proxy.initiate_chat(coder, message=task)
