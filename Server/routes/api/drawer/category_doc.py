CATEGORY = {
    'tags': ['Drawer'],
    'description': '카테고리 리스트 조회',
    'responses': {
        '200': {
            'description': '리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'category_code': 1,
                        'category_name': '캐릭터',
                        'chosen': 15
                    },
                    {
                        'category_code': 2,
                        'category_name': '음식',
                        'chosen': 11
                    }
                ]
            }
        }
    }
}

CATEGORY_SELECT = {
    'tags': ['Drawer'],
    'description': '카테고리 선택',
    'parameters': [
        {
            'name': 'code',
            'description': '선택한 카테고리 코드',
            'in': 'formData',
            'type': 'int'
        }
    ],
    'responses': {
        '201': {
            'description': '카테고리 선택 성공. 할당된 Shower의 id와 점수 책정을 위한 이미지 이름 반환',
            'examples': {
                'application/json': {
                    'shower_id': 'a1zdp584a8tod94jla011v1c5',
                    'image_name': 'character_01'
                }
            }
        }
    }
}
