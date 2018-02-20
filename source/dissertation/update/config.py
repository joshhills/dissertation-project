messaging = {
    'host': 'localhost',
    'queues': {
        'work_update': 'work_update_queue',
        'global_error': 'global_error'
    }
}

# Database settings
database = {
    'host': 'couchbase://database',
    'username': 'root',
    'password': 'administrator'
}

api_url = 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v1?maxlength=1&appid={0}&count={1}'
