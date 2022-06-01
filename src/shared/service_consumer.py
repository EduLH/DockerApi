from requests import get


async def get_info(query_params):
    result = get("https://jsonplaceholder.typicode.com/todos/", params=query_params)
    return result
