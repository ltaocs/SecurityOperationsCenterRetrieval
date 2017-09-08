with open('old.csv', 'r') as t1:
    old_csv = t1.readlines()
with open('new.csv', 'r') as t2:
    new_csv = t2.readlines()

with open('update.csv', 'w') as out_file:
    line_in_new = 0
    line_in_old = 0
    while line_in_new < len(new_csv) and line_in_old < len(old_csv):
        if old_csv[line_in_old] != new_csv[line_in_new]:
            out_file.write(new_csv[line_in_new])
        else:
            line_in_old += 1
        line_in_new += 1
