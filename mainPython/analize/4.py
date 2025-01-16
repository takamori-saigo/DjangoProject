import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vacancies_processed.csv')

df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')
df['year'] = df['published_at'].dt.year

frontend_keywords = ['Python-программист', 'python', 'питон', 'пайтон']

df_frontend = df[df['name'].str.contains('|'.join(frontend_keywords), case=False, na=False)]

df_frontend = df_frontend.dropna(subset=['year'])

salary_by_year = (
    df_frontend.groupby('year')['salary_rub']
    .mean()
    .reset_index()
    .rename(columns={'salary_rub': 'avg_salary_rub'})
)

vacancy_count_by_year = (
    df_frontend.groupby('year')['name']
    .count()
    .reset_index()
    .rename(columns={'name': 'vacancy_count'})
)


plt.figure(figsize=(12, 6))
plt.plot(salary_by_year['year'], salary_by_year['avg_salary_rub'], marker='o', color='b')
plt.title('Динамика уровня зарплат питонистов по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата (RUB)')
plt.grid(True)
plt.savefig('frontend_salary_trend.png')
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(vacancy_count_by_year['year'], vacancy_count_by_year['vacancy_count'], marker='o', color='g')
plt.title('Динамика количества вакансий питонистов по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.grid(True)
plt.savefig('frontend_vacancy_trend.png')
plt.close()

result = pd.merge(salary_by_year, vacancy_count_by_year, on='year', how='outer')
result.to_csv('frontend_analytics_results.csv', index=False)

