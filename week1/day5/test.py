raw = "   user:  ALIce-joHN   | score:  0042.756  | active: YES   "

splitted = raw.split('|')
user = splitted[0].strip().split(':');
score = splitted[1].strip().split(':');
active = splitted[2].strip().split(':');

result = ' | '.join([
    ': '.join([user[0].strip().capitalize(), user[1].strip().title()]),
    ': '.join([score[0].strip().capitalize(), f"{float(score[1]):0<.1f}"]),
    ': '.join([active[0].strip().capitalize(), active[1].strip().lower()]),
])

print(result)


test = 'User: Alice-John | Score: 42.8 | Active: yes'
print(test == result)