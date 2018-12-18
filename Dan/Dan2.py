
def select_info_prof(prof_name, city):	

    i_data_info={}
    vacancies_by_criteria = [vacancy for vacancy in v if vacancy.get('name').count(prof_name) and vacancy.get('area').get('name') == city]
    i_data_info["Количество вакансий"] = len(vacancies_by_criteria)
    salaries = [vacancy.get('salary') for vacancy in vacancies_by_criteria if vacancy.get('salary')]
    salaries_rur = [salary for salary in salaries if salary.get('currency') == 'RUR']
    salaries_rur_from_gross = [salary.get('from')*0.87 for salary in salaries_rur if salary.get('from') and salary.get('gross')]
    salaries_rur_from = [salary.get('from') for salary in salaries_rur if salary.get('from') and not salary.get('gross')]
    salaries_rur_from_all = salaries_rur_from + salaries_rur_from_gross
    i_data_info["Средняя_зп_мин"] = round( sum(salaries_rur_from_all) / len(salaries_rur_from_all)) if salaries_rur_from_all else "нет данных"

    raw_key_skills = [vacancy.get('key_skills') for vacancy in vacancies_by_criteria if len(vacancy.get('key_skills')) != 0]	
    key_skills = [key_skill.get('name') for item in raw_key_skills for key_skill in item]
    ks_entries_count_by_number = {key_skills.count(skill) : skill for skill in key_skills}
    keys_sort=sorted(ks_entries_count_by_number.items(), key=lambda x: x[0], reverse=True)
    top5_ks=keys_sort[:5]
    top_ = [ks[1] for ks in top5_ks] if len(ks_entries_count_by_number) >2 else "нет данных" 
    i_data_info["Топ5_Скилов"]=top_
    return i_data_info
        
search_prof=["Системный аналитик", "Бизнес аналитик"]
cities = set([vacancy.get('area').get('name') for vacancy in v])
data_info = {}
data_info = {prof_name : {city : select_info_prof(prof_name, city) for city in cities} for prof_name in search_prof}
