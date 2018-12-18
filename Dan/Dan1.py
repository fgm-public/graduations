
salaries = [vacancy.get('salary') for vacancy in full_vacancies if vacancy.get('salary')]

salaries_rur = [salary for salary in salaries if salary.get('currency') == 'RUR']

salaries_rur_from_gross = [salary.get('from')*0.87 for salary in salaries_rur if salary.get('from') and salary.get('gross')]

salaries_rur_from = [salary.get('from') for salary in salaries_rur if salary.get('from') and not salary.get('gross')]

salaries_rur_from_all = salaries_rur_from + salaries_rur_from_gross

salaries_rur_from_sum = round( sum(salaries_rur_from_all) / len(salaries_rur_from_all))
