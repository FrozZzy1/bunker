import random
import string


async def generate_room_code(length: int = 4) -> str:
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))
