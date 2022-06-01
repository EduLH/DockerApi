from src.shared.service_consumer import get_info


async def user_query(user_id):
    response = await get_info({'userId': user_id})
    return response


async def id_query(id):
    response = await get_info({'id': id})
    return response


async def completed_query(completed):
    response = await get_info({'completed': completed})
    return response


async def title_query(title):
    response = await get_info({'title': title})
    return response


async def all_query(req_data):
    user_id = req_data.get('user_id', '')
    id = req_data.get('id', '')
    completed = req_data.get('completed', '')
    title = req_data.get('title', '')
    params = {
        'userId': user_id,
        'id': id,
        'completed': completed,
        'title': title
    }
    response = await get_info(params)
    return response

async def search_like(req_data):
    user_id = req_data.get('user_id', '')
    id = req_data.get('id', '')
    completed = req_data.get('completed', '')
    title = req_data.get('title', '')
    response = await get_info({})
    filtered_response = [item for item in response.json() if (
            item['userId'] == user_id or
            item['id'] == id or
            item['completed'] == completed or
            title in item['title']
    )]
    return filtered_response
