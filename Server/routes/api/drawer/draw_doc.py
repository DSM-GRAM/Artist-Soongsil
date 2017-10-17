DRAW = {
    'tags': ['Drawer'],
    'description': '그리기 시작',
    'parameters': [
        {
            'name': 'shower_id',
            'description': '카테고리 선택 시 할당된 shower id',
            'in': 'formData',
            'type': 'str'
        }
    ],
    'responses': {
        '201': {
            'description': '그리기 시작 성공'
        }
    }
}

SCORE = {
    'tags': ['Drawer'],
    'description': '점수 측정(미구현)',
    'parameters': [
        {
            'name': 'image',
            'description': '사용자가 그린 이미지',
            'in': 'formData',
            'type': 'file'
        },
        {
            'name': 'origin_image_name',
            'description': '카테고리 선택 시 할당된 image name',
            'in': 'formData',
            'type': 'str'
        }
    ],
    'responses': {
        '201': {
            'description': '점수 측정 성공',
            'examples': {
                'application/json': {
                    'score': 123
                }
            }
        }
    }
}
