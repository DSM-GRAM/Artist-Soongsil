RANKING = {
    'tags': ['LeaderBoard'],
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
    'tags': ['LeaderBoard'],
    'description': '사용자 이미지 조회',
    'parameters': [
        {
            'name': 'phone',
            'description': '이미지를 조회할 핸드폰 번호',
            'in': 'query',
            'type': 'str'
        }
    ],
    'responses': {
        '200': {
            'description': '이미지 조회 성공. 이미지 반환'
        }
    }
}
