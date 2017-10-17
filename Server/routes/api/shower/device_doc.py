DEVICE = {
    'tags': ['Shower'],
    'description': '',
    'parameters': [
        {
            'name': 'registration_id',
            'description': '디바이스의 Firebase Token',
            'in': 'formData',
            'type': 'str'
        }
    ],
    'responses': {
        '201': {
            'description': '디바이스 등록 완료'
        }
    }
}
