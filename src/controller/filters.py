from service_consumer import get_info


async def user_query(user_id):
    response = get_info({'userId': user_id})
    return response


async def id_query(id):
    response = get_info({'id': id})
    return response


async def completed_query(completed):
    response = get_info({'completed': completed})
    return response


async def title_query(title):
    response = get_info({'title': title})
    return response


async def all_query(**kwargs):
    user_id = kwargs.get('user_id', '')
    id = kwargs.get('id', '')
    completed = kwargs.get('completed', '')
    title = kwargs.get('title', '')
    params = {
        'user_id': user_id,
        'id': id,
        'completed': completed,
        'title': title
    }
    # query += f"?userId={user_id}" if user_id else ''
    # query += f"?id={id}" if id else ''
    # query += f"?completed={completed}" if completed else ''
    # query += f"?title={title}" if title else ''

    response = get_info(params)
