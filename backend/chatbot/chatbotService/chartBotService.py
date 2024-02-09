import os
from openai import OpenAI
client = OpenAI(
    api_key='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',
)

def update_list(message, pl):
    pl.append(message)


def create_prompt(message, pl):
    p_message = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt = ''.join(pl)
    return prompt

def get_api_response(prompt):
    try:
        response = client.completions.create(
          model="gpt-3.5-turbo-instruct-0914",
          prompt=prompt,
          max_tokens=100,
          temperature=0,
          stop=[' Human:', ' AI:']
        )
        return response.choices[0].text
    except Exception as e:
        print('error', e)
        
def get_bot_response(message, pl):
    prompt = create_prompt(message, pl)
    bot_response = get_api_response(prompt)
    if bot_response:
        update_list(bot_response, pl)
        pos = bot_response.find("\nAI: ")
        # bot_response = bot_response[pos + 4:]
        bot_response = bot_response[pos + 4:]
    else:
        bot_response = "Something went wrong..."
    return bot_response