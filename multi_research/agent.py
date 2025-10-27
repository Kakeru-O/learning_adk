from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.tools import google_search

# --- 1. 個々の専門エージェントの定義 ---

# 🔹 役割 1: リサーチ専門エージェント (ツールを使用)
# このエージェントは、ユーザーのクエリに基づいてGoogle検索を実行し、
# その結果をセッションの状態（state）に保存します。
# output_key="research_results" を指定することで、次のエージェントがこの結果を利用できるようになります。
researcher_agent = LlmAgent(
    name="ResearcherAgent",
    model="gemini-2.5-flash",
    description="最新の事実情報を見つけるためのGoogle検索ツール専門家。",
    instruction=(
        "あなたは最高の情報リサーチャーです。与えられたトピックについて、"
        "必ずGoogle検索ツールを使用して情報を集めてください。"
    ),
    tools=[google_search],
    output_key="research_results"  # 結果を 'research_results' というキーでセッションに保存
)

# 🔹 役割 2: 要約専門エージェント (共有されたデータを利用)
# このエージェントは、前のエージェントがセッションに保存したデータを利用して要約します。
# 実際には、LLMがInstructionと共有データ（research_results）の両方を考慮して応答を生成します。
summarizer_agent = LlmAgent(
    name="SummarizerAgent",
    model="gemini-2.5-flash",
    description="与えられた情報を簡潔かつ包括的に要約する専門家。",
    instruction=(
        "あなたはリサーチャーから提供された情報を、一般の読者向けに**3行以内で**"
        "分かりやすく、魅力的に要約する専門家です。"
    )
)

# --- 2. ワークフローエージェントによる結合 ---

# 🔸 ルートエージェント: SequentialAgent
# 専門エージェントを順番に実行するワークフローを定義します。
# SequentialAgentはLLMを使わず、定義された順序（Researcher -> Summarizer）で実行を制御する、
# 「ディスパッチャー（Dispatcher）」のような役割です。
root_agent = SequentialAgent(
    name="ResearchSummarizer",
    description="Google検索で情報を収集し、それを要約する2段階のワークフローを実行します。",
    sub_agents=[
        researcher_agent,  # 1. リサーチエージェントを実行
        summarizer_agent   # 2. 要約エージェントを実行（リサーチ結果を参照可能）
    ]
)