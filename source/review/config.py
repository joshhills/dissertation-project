message_queue = {
    'host': 'localhost',
    'queues': {
        'work_review': 'work_review_queue',
        'global_error': 'global_error'
    }
}

api_url = 'http://store.steampowered.com/appreviews/{0}?json=1&filter=recent&language=all&purchase_type=all&start_offset={1}'