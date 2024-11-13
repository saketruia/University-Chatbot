import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure your Gemini API key
genai.configure(api_key=os.getenv('API_KEY'))

def index(request):
    return render(request, 'chatbot.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        user_message = json.loads(request.body)['message']
        
        try:
            model = genai.GenerativeModel("tunedModels/univchatbot-enhanced-az6s43uad40q")
            response = model.generate_content(user_message)

            if response is None:
                raise ValueError("Invalid response from the AI service.")

            bot_message = response.text
            return JsonResponse({'message': bot_message})

        except Exception as e:
            bot_message = f'{e} '

        return JsonResponse({'message': bot_message})



