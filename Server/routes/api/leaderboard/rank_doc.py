RANKING = {
    'tags': ['리더보드'],
    'description': '랭킹 조회',
    'responses': {
        '200': {
            'description': '랭킹 조회 성공(점수 높은 순)',
            'examples': {
                'application/json': [
                    {
                        'name': '정다은',
                        'phone': '112',
                        'affiliation': '경찰서',
                        'score': 5959
                    },
                    {
                        'name': '정민철',
                        'phone': '01082829595',
                        'affiliation': '병찬이의 마음속',
                        'score': 486
                    }
                ]
            }
        }
    }
}

DREW_IMAGE = {
    'tags': ['리더보드']
}
