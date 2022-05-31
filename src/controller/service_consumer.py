from requests import get

async def get_info():
    result = get('https://jsonplaceholder.typicode.com/todos')
    return result
