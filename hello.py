from litellm import completion
from config import PROVIDER_MODEL as MODEL

resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are teacher."},
        {"role": "user", "content": "Say hello in 3 language."}
    ],
    max_tokens=32, #ขอคำตอบไม่เกิน 32 token
)
print("REPLY:", resp.choices[0].message["content"]) 
print("USAGE:", getattr(resp, "usage", {}))