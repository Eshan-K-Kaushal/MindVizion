'''
author: Eshan K Kaushal
'''
import pandas as pd
class Script_Maker:
    def script_maker(self):
        categories_of_ques = ['Their Introduction', 'Their background', 'Their religious beliefs',
                              'Their definition of a perfect day',
                              'Their daily routine',
                              'Where and what they do for work and what they like and dont like about their work',
                              'Things they like', 'Things they dont like', 'Their Pet Peeves',
                              'About their family', 'About their family life',
                              'Their favorite color', 'Things they like to eat',
                              'activities they like', 'activities they dont like',
                              'what they would do to make someone who is sad - happy', 'what they would do if someone is mad at them',
                              'what they would do to help a family member if they are down with a sickness',
                              'Their major source of influence/inspiration', 'Their favorite virtual character',]

        list_of_ques = ['Please introduce yourself in 5-6 lines. The more you tell the better.',
                        'Give me some background on yourself - your roots, your origin, your childhood.',
                        'What are your religious beliefs?',
                        'How would you define a perfect day?', 'Describe your daily routine to me - from morning to the evening.',
                        'Please tell me about what you do for work - also please tell me what you like about it and what you dont like about it',
                        'Tell me about the things you like', 'Now tell me about the things you dont like',
                        'Now please tell me about your pet peeves - something that you or a particular person would find absolutely annoying.',
                        'What can you tell me about your family - give me a little background',
                        'Take me through your family life - by this I mean tell me about how well you gel with your family members, who do you love the most, how do you spend time with them and what do you do for them to make them happy!',
                        'What is your favorite color?', 'What are the things you like to eat - your favorite kind of foods, cuisines, snacks?',
                        'What activities - outdoors and indoors - do you like? Also tell me about the activities you take part in when you are free', 'And, what activities you dont like to do at all?',
                        'How would you cheer up who is sad?', 'How would you deal with someone who is angry/mad at you?',
                        'what would you do to help a family member who is sick?',
                        'who has influenced/inspired you the most and why?', 'who is your most favorite movie/comic/game/tv-show character and why?',
                        'what phrases or words do you use when you want to want to make someone feel better, happy, loved, respected or cared for?',
                        'what phrases or words do ',
                        ]

        print(len(list_of_ques), len(categories_of_ques))

        idk = ['idk', 'i dont know', 'i dont know how to answer that',
               'dont really know how to answer that one',
               'dont have any answers to that']

        myself = ['myself', 'Myself', 'MYSELF']
        someone = ['someone else', 'some one else', 'SOMEONEELSE', 'someoneelse', 'somebody else', 'some body else']

        ans_to_questions = []

        print('Welcome to the Consciousness Mapper')
        print('Are you trying to emulate yourself or someone else?')
        usr_choice = input("Say - 'myself' if you are emulating yourself or 'someone else' if you are trying to emulate someone you know: ")
        if usr_choice.lower() in someone:
            print('So you are trying to emulate someone you know.')
            usr_name = input('What is their name?: ')
            for i in list_of_ques:
                i = i.replace('yourself', 'them').replace('your', 'their').replace('you', 'they')
                print(i)
        if usr_choice.lower() in myself:
            print('Alrighty!')
            usr_name = input('What is your name?: ')
        else:
            print('Typing error')
            print('System set to default - Self emulation.')
            print('NOTE: If emulating someone else - answer the questions the way they would for best performance,')
            usr_name = input('What is your/their name?: ')
        print('If you cant answer a question then just say/type - I dont know how to answer that.')

        for i in range(len(list_of_ques)):
            print(list_of_ques[i])
            usr_inp = input('User: ')
            if len(usr_inp.split()) <= 4:
                print('Please give a longer and more detailed answer for better emulation.')
                usr_inp = input('Try again: ')
                if len(usr_inp.split()) <= 4:
                    print('Length is still not good but will be considering this answer.')
                    ans_to_questions.append(usr_inp)
            if usr_inp in idk:
                print('So you dont know - will be defaulting to mass population.')
                ans_to_questions.append('Just like any other human.')
            else:
                ans_to_questions.append(usr_inp)
            # print(ans_to_questions)
        print(ans_to_questions)
        df_dict = {'categories_of_ques': categories_of_ques,
                   'list_of_ques': list_of_ques,
                   'ans_to_ques': ans_to_questions}
        pd.set_option('display.max_column', None)
        df = pd.DataFrame.from_dict(df_dict)
        print(df)

        pre_prompt = 'I am a great actor. I will act as the person in the following context and will interact with the user like this person when prompted to talk or greeted by a user. I will act as if I am meeting the user in person. The context has been divided into categories. Use the context from the categories when a question pertaining to that category is asked:\nContext: \n'
        prompt_final = pre_prompt
        for i in range(len(categories_of_ques)):
            prompt_final += str(categories_of_ques[i]) + ':\n' + str(ans_to_questions[i]) + '\n'
        prompt_final += '\n\n <<BLOCK>>'

        text_file = open(f"{usr_name.lower()}.txt", "w")
        text_file.write(prompt_final)
        text_file.close()

