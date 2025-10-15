def round_to_nearest_2_5(x):
    return round(x / 2.5) * 2.5

def format_weight(w):
    if w.is_integer():
        return int(w)
    return w

programma = {
    '1week': [70, 5, 5],
    '2week': [72.5, 5, 5],
    '3week': [75, 4, 5],
    '4week': [85, 3, 3],
    '5week': [88, 4, 2],
    '6week': [70, 3, 5],
    '7week': [77.5, 5, 4],
    '8week': [87.5, 3, 2],
    '9week': [90, 3, 2],
    '10week': [70, 3, 3],
    '11week': [85, 2, 2],
    '12week': [105, 1, 1]
}

max_lift = float(input(''))

new_programma = {}
for week, values in programma.items():
    percent = values[0] / 100
    sets = values[1]
    reps = values[2]
    raw_weight = max_lift * percent
    rounded_weight = round_to_nearest_2_5(raw_weight)
    rounded_weight = format_weight(rounded_weight)
    new_programma[week] = [rounded_weight, sets, reps]

print(new_programma)
