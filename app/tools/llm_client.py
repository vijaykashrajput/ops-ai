# import os
# from openai import OpenAI

# class LLMClient:
#     def __init__(self):
#         self.client = OpenAI(api_key=os.getenv("sk-bab598bbaa104c69802edbbc3ce0e496"))

#     def analyze_logs(self, logs: str) -> dict:
#         prompt = f"""
#         You are a DevOps expert.

#         Analyze the following logs and return:
#         1. Root cause
#         2. Severity (low/medium/high)
#         3. Suggested fix

#         Logs:
#         {logs}

#         Respond in JSON format.
#         """

#         response = self.client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": prompt}]
#         )

#         content = response.choices[0].message.content

#         return content
import os
from openai import OpenAI

class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAPI_KEY"),
            # base_url="https://api.deepseek.com"
        )

    def analyze_logs(self, logs: str) -> dict:
        prompt = f"""
        You are a DevOps expert.

        Analyze logs and return JSON:
        {{
          "root_cause": "...",
          "severity": "...",
          "suggested_fix": "..."
        }}

        Logs:
        {logs}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content

        return content