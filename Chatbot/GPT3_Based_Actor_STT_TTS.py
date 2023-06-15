'''
author: Eshan K Kaushal
'''
import os
import openai
from random import choice
import speech_recognition as sr
import pyttsx3

s_rec = sr.Recognizer()
engine = pyttsx3.init()

def say_text(command):
  # Initialize the engine
  engine.say(command)
  engine.runAndWait()

class Chatbot:

  PATH = '/content/MindVizion/Chatbot/key.txt'
  txt_files = []
  for file in os.listdir('/content/MindVizion/Chatbot/'):
    if file.endswith('.txt'):
      txt_files.append(file)

  def open_file(self, file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
      return infile.read()

  def chat(self):
    usr_name = input('Please type the name of the Person you are trying to Emulate: ')
    usr_name = usr_name.lower()
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
    if f'{actor_name}.txt' not in self.txt_files:
      print('Defaulting to Preset since the spellings were wrong')
      print(f'Wolff: Hi! Nice to see you here today!')
    else:
      print(f'{usr_name}: Hi! Nice to see you here today!')
    while True:
      with sr.Microphone() as source2:
        s_rec.adjust_for_ambient_noise(source2, duration=0.2)
        print("User: ")
        audio2 = s_rec.listen(source2)
        try:
          u_input = s_rec.recognize_google(audio2)
          u_input = u_input.lower()
        except sr.UnknownValueError:
          print('No clarity: reduce noise')
      #u_input = input('User: ')
      conversation.append('User: %s' % u_input)
      text_block = '\n'.join(conversation)
      if f'{actor_name}.txt' not in self.txt_files:
        # print('Defaulting to Preset since the spellings were wrong!')
        # print('Available Text files are: ', self.txt_files)
        prompt =self.open_file(f'/content/MindVizion/Chatbot/wolff.txt').replace('<<BLOCK>>', text_block)
        #print(prompt)
        prompt = prompt + f'\nWolff: '
        response = actor_gpt3(prompt)
        print(f"Wolff: ", response)
        say_text(response)
        conversation.append(f'Wolff: %s'%response)
        if 'bye' in u_input.split() or 'take care' in u_input:
          break
      else:
        prompt =self.open_file(f'/content/MindVizion/Chatbot/{usr_name}.txt').replace('<<BLOCK>>', text_block)
        #print(prompt)
        prompt = prompt + f'\n{usr_name}: '
        response = actor_gpt3(prompt)
        print(f"{usr_name}: ", response)
        say_text(response)
        conversation.append(f'{usr_name}: %s'%response)
        if 'bye' in u_input.split() or 'take care' in u_input:
          break


