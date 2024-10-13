task_done_cnt = 12
hours_spent_cnt = 1.5
course_name = 'Python'
time_per_task = hours_spent_cnt / task_done_cnt
print(
    'Курс: ', course_name,
    ', всего задач: ', task_done_cnt,
    ', затрачено часов: ', hours_spent_cnt,
    ', среднее время выполнения: ', time_per_task, ' часа.',
    sep='')