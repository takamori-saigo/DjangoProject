import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vacancies_processed.csv')

keywords = ['Python-программист', 'python', 'питон', 'пайтон']
filtered_data = data[data['name'].str.contains('|'.join(keywords), case=False, na=False)]

top10_salary = (filtered_data.groupby('area_name')['salary_rub']
                 .mean()
                 .sort_values(ascending=False)
                 .head(10))
top10_salary.to_csv('city_salary.csv')

plt.figure(figsize=(12, 6))
top10_salary.plot(kind='bar', color='skyblue')
plt.title('Уровень зарплат по городам (Топ-10)')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата (RUB)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('city_salary.png')
plt.close()

top10_vacancy = (filtered_data['area_name']
                  .value_counts(normalize=True)
                  .head(10))
top10_vacancy.to_csv('city_vacancy_share.csv')

plt.figure(figsize=(12, 6))
top10_vacancy.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title('Доля вакансий по городам (Топ-10)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('city_vacancy_share.png')
plt.close()

