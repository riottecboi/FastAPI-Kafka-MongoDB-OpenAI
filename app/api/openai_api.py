from openai import OpenAI
from core.config import settings

async def get_openai_recommendation(request_data):
    try:
        client = OpenAI(api_key=settings.OPENAI_KEY)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Provide three recommendations for doing in {request_data['country']} during {request_data['season']}.",
                }
            ],
            model="gpt-3.5-turbo",
        )
        return [chat_completion.choices[0].message.content]
    except Exception as e:
        raise Exception(str(e))