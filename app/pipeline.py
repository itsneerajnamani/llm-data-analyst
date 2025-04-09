import pandas as pd
from app.llm_engine import ask_llm
from app.utils import clean_data, generate_summary

async def analyze_file(file):
    df = pd.read_csv(file.file)
    df = clean_data(df)

    summary = generate_summary(df)

    insight_prompt = f"Perform EDA and provide business insights for this dataframe:\n{summary}"
    insights = ask_llm(insight_prompt)

    viz_prompt = f"Create matplotlib/seaborn code for 2 useful charts using this dataframe summary:\n{summary}"
    code_response = ask_llm(viz_prompt)

    return {"insights": insights, "code_snippets": code}