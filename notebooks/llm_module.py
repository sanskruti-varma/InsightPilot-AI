def create_llm_prompt(llm_input):
    prompt = f"""
You are a business analytics assistant for InsightPilot AI.

Analyze the following verified business information:

Prediction:
{llm_input["prediction"]}

Model:
{llm_input["model"]}

Features used:
{llm_input["features_used"]}

Feature explanations:
{llm_input["feature_explanations"]}

Business insights:
{llm_input["business_insights"]}

Recommendations:
{llm_input["recommendations"]}

Provide:
1. A short business summary
2. Key insights
3. Three practical recommendations

Rules:
- Use only the information provided.
- Do not invent numerical values.
- Keep the language simple and professional.
"""
    return prompt