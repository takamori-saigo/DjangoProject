import requests
from datetime import datetime, timedelta

API_URL = 'https://api.hh.ru/vacancies'

HEADERS = {'User-Agent': 'Django App'}

def get_last_vacancies():
    params = {
        'text': 'Frontend-программист',
        'search_field': 'name',
        'date_from': (datetime.utcnow() - timedelta(days=1)).isoformat(),
        'per_page': 10,
        'order_by': 'publication_time'
    }

    response = requests.get(API_URL, headers=HEADERS, params=params)

    response.raise_for_status()

    vacancies = response.json().get('items', [])
    
    result = []
    for vacancy in vacancies:
        vacancy_data = {
            'title': vacancy.get('name'),
            'company': vacancy.get('employer', {}).get('name'),
            
            'salary': vacancy.get('salary', {}).get('from') if vacancy.get('salary') else 'Не указана',

            'region': vacancy.get('area', {}).get('name'),

            'published_at': vacancy.get('published_at'),

            'vacancy_url': vacancy.get('alternate_url'),
        }
        
        vacancy_detail_response = requests.get(
            f"{API_URL}/{vacancy.get('id')}",
            headers=HEADERS
        )
        vacancy_detail = vacancy_detail_response.json()

        vacancy_data['description'] = vacancy_detail.get('description', 'Описание не указано')

        vacancy_data['skills'] = ', '.join(
            skill['name'] for skill in vacancy_detail.get('key_skills', [])
        )
        
        result.append(vacancy_data)
    return result
