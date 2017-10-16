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
