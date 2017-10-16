INFORMATION = {
    'tags': ['Drawer'],
    'description': '사용자 정보 입력',
    'parameters': [
        {
            'name': 'phone',
            'description': '핸드폰 번호',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'name',
            'description': '이름',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'age',
            'description': '나이',
            'in': 'formData',
            'type': 'int'
        },
        {
            'name': 'affiliation',
            'description': '소속',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'score',
            'description': '점수',
            'in': 'formData',
            'type': 'int'
        },
        {
            'name': 'image',
            'description': '사용자가 그린 그림',
            'in': 'formData',
            'type': 'file'
        }
    ],
    'responses': {
        '201': {
            'description': '사용자 정보 입력 성공'
        }
    }
}
