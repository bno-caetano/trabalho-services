import openai
from openai import OpenAI
import os
import streamlit as st

class TextCompletion:

    def __init__(self, prompt, num_token, key):
        # self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_key = key
        self.client = OpenAI(api_key=self.api_key)
        self.all_responses = list()
        self.prompt = prompt
        self.num_token = num_token

    def chunk_response(self):
        if self.num_token > 4096:
            step = 2000
            for i in range(0,len(self.prompt), step):

                print('Processo de chunk iniciado:')

                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Summarize the following text in original language within 150 words"},
                        {"role": "assistant", "content": "Yes."},
                        {"role": "user", "content": self.prompt[i:i+step]},
                    ],
                )

                self.all_responses += response.choices[0].message.content
        else:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Summarize the following text in original language"},
                    {"role": "assistant", "content": "Yes."},
                    {"role": "user", "content": self.prompt},
                ],
            )

            self.all_responses += response.choices[0].message.content

    def final_response(self):

        self.chunk_response()

        response_summarize = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the following text in original language"},
            {"role": "assistant", "content": "Yes."},
            {"role": "user", "content": ''.join(self.all_responses)},
        ],
    )

        return response_summarize.choices[0].message.content
