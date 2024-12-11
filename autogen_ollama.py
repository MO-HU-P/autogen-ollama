import streamlit as st
import autogen

def setup_autogen_agents(model_name, base_url):
    config_list = [
        {
            'base_url': base_url,
            'api_key': "dummy_key",
            'model': model_name,
        }
    ]

    llm_config = {
        "config_list": config_list,
        "temperature": 0.7
    }

    assistant = autogen.AssistantAgent(
        name="Assistant",
        system_message="You are a helpful AI assistant.",
        llm_config=llm_config
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").strip().endswith("TERMINATE")
    )

    return assistant, user_proxy

def run_chat(assistant, user_proxy, user_message):
    try:
        user_proxy.initiate_chat(assistant, message=user_message)
        conversation_messages = assistant.chat_messages[user_proxy]
        
        return conversation_messages
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")

        return []

def display_conversation(conversation):
    for msg in conversation:
        sender = msg.get('name', 'Unknown')
        content = msg.get('content', '')
        
        if sender == 'user_proxy':
            st.chat_message("user").write(content)
        else:
            st.chat_message("assistant").write(content)

def main():
    st.title("Autogenアプリ")
    with st.sidebar:
        st.header("設定")
        model_name = st.text_input("モデル名", "dsasai/llama3-elyza-jp-8b")
        base_url = st.text_input("Base URL", "http://localhost:11434/v1")

    user_message = st.chat_input("メッセージを入力してください")

    if user_message:
        assistant, user_proxy = setup_autogen_agents(model_name, base_url)

        with st.spinner('処理中...'):
            conversation = run_chat(assistant, user_proxy, user_message)

        if conversation:
            display_conversation(conversation)

if __name__ == "__main__":
    main()