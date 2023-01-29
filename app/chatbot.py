import openai
from .settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
completion = openai.Completion()


def ask(question):
    prompt = f'Human: {question} \nAI:'
    req = completion.create(
        prompt=prompt,
        engine='davinci',
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=1,
        stop=['Human', "AI", "Dexter"]
    )

    answer = req.choices[0].text

    return answer
