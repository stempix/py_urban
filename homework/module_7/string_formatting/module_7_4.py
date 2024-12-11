# Variables
team1_name = "Мастера кода"
team2_name = "Волшебники данных"

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

challenge_result = ''
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = f"победа команды {team1_name}!"
elif score_2 > score_1 or (score_2 == score_1 and team2_time < team1_time):
    challenge_result = f"победа команды {team2_name}!"
else:
    challenge_result = "ничья!"

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

# %-formatting
print("В команде %s участников: %d!" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %(team1)d и %(team2)d!" % {"team1": team1_num, "team2": team2_num})

# Format by .format()
print("Команда {0} решила задач: {1}!".format(team2_name, score_2))
print("{team_name} решили задачи за {time} с.!".format(time=team1_time, team_name=team1_name))

# F-string formatting
print(f"Команды решили {score_1} и {score_2} задач соответственно.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено задач: {tasks_total}, в среднем по {time_avg.__round__(2)} секунды на задачу!")