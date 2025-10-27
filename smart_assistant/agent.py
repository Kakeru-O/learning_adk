from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

# エージェントの定義
root_agent = Agent(
    # エージェント名
    name="SmartAssistant",
    
    # 使用するLLMモデル（環境に合わせて適宜変更してください）
    model="gemini-2.5-flash", 
    
    # エージェントの簡単な説明
    description="質問に答えるためのGoogle検索機能を備えた有能なアシスタント。",
    
    # LLMへの指示（ペルソナ）
    instruction=(
        "あなたは親切で正確なアシスタントです。ユーザーの質問に対して、"
        "可能な限りGoogle検索ツールを使用して事実に基づいた情報を提供してください。"
    ),
    
    # ツールリストにgoogle_searchを追加
    tools=[google_search] 
)