'''
author: Eshan K Kaushal
'''
import os
import openai
from random import choice

class Chatbot:

  PATH = '/content/MindVizion/Chatbot/key.txt'

  def open_file(self, file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
      return infile.read()

  def chat(self):
    usr_name = input('Please type the name of the Person you are trying to Emulate: ')
    actor_name = usr_name.lower()
    openai.api_key = self.open_file(self.PATH)

    def actor_gpt3(prompt, model="text-davinci-003",
        temperature=1, max_tokens=512, top_p=1, frequency_penalty=1,
                   presence_penalty=0.25, stop=['User:']):

      prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
      response = openai.Completion.create(
        engine = model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty = frequency_penalty,
        presence_penalty = presence_penalty,
        stop=stop
        )

      text = response['choices'][0]['text'].strip()
      return text

    conversation = list()
    print(f'{actor_name}: Hi! Nice to see you here today!')
    while True:
      u_input = input('User: ')
      conversation.append('User: %s' % u_input)
      text_block = '\n'.join(conversation)
      prompt =self.open_file(f'/content/MindVizion/Chatbot/{usr_name}.txt').replace('<<BLOCK>>', text_block)
      #print(prompt)
      prompt = prompt + f'\n{usr_name}: '
      response = actor_gpt3(prompt)
      print(f"{usr_name}: ", response)
      conversation.append(f'{usr_name}: %s'%response)
      if 'bye' in u_input.split() or 'take care' in u_input:
        break


