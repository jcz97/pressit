from django.shortcuts import render
from django.conf import settings
import openai

def generate_sentence(request):
    openai.api_key = settings.OPENAI_API_KEY
    if request.method == 'POST':
        response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a funny and helpful assistant.",
            },
            {"role": "user", "content": "Come up with a funny way of asking 'why did you press that button?'"},
        ],
        temperature=1,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
        sentence = response.choices[0].message["content"].strip()
        return render(request, 'pressit/generate.html', {'sentence': sentence})
    return render(request, 'pressit/generate.html')
