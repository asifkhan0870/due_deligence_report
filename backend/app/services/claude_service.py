import anthropic
import asyncio
from app.config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

async def generate_report_async(prompt):
    loop = asyncio.get_event_loop()

    response = await loop.run_in_executor(
        None,
        lambda: client.messages.create(
            model="claude-haiku-4-5-20251001",  # ✅ FIXED MODEL
            max_tokens=3000,
            temperature=0.3,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    )

    return response.content[0].text