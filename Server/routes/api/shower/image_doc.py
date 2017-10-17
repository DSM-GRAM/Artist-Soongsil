SAMPLE_IMAGE = {
    'tags': ['Shower'],
    'description': '',
    'parameters': [
        {
            'name': 'image_name',
            'description': '조회할 샘플 이미지의 이름',
            'in': 'query',
            'type': 'str'
        }
    ],
    'responses': {
        '200': {
            'description': '이미지 조회 완료. 샘플 이미지 반환',
        }
    }
}
