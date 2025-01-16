import pandas as pd
import re
from collections import Counter

file_path = 'vacancies_processed.csv' 
df = pd.read_csv(file_path)

keywords = [
    'Python-программист', 'python', 'питон', 'пайтон'
]

def is_project_lead(title):
    title_lower = str(title).lower()
    return any(keyword in title_lower for keyword in keywords)

df_filtered = df[df['name'].apply(is_project_lead)].copy()

df_filtered.loc[:, 'year'] = pd.to_datetime(df_filtered['published_at'], errors='coerce').dt.year

df_filtered['key_skills'] = df_filtered['key_skills'].fillna('')

skills_by_year = df_filtered.groupby('year')['key_skills'].apply(lambda x: '\n'.join(x)).reset_index()

top_skills_by_year = []

for year, skills in zip(skills_by_year['year'], skills_by_year['key_skills']):
    skills_list = re.split(r'\r?\n|\r', skills)
    skills_list = [skill.strip() for skill in skills_list if skill.strip()]
    
    skill_counts = Counter(skills_list)
    top_20_skills = skill_counts.most_common(20)
    
    for skill, freq in top_20_skills:
        top_skills_by_year.append({'year': year, 'skill': skill, 'frequency': freq})

top_skills_df = pd.DataFrame(top_skills_by_year)

top_skills_df.to_csv('top_20_skills_by_year.csv', index=False)
