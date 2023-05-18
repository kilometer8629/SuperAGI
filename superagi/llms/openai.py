import os
import json
from abc import ABC, abstractmethod

import openai
from superagi.llms.base_llm import BaseLlm


class OpenAi(BaseLlm):
    def __init__(self, model="gpt-4", temperature=0.3, max_tokens=3600, top_p=1, frequency_penalty=0,
                 presence_penalty=0, number_of_results=1):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.number_of_results = number_of_results

    def chat_completion(self, messages):
        try:
            print("Messages:", messages)
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.ChatCompletion.create(
                n=self.number_of_results,
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )
            content = response.choices[0].message["content"]
            return {"response": response, "content": content}
        except Exception as exception:
            print("Exception:", exception)
            return {"error": exception}