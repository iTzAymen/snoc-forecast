import csv

dump_file = 'DBSS_SNOC_ACTIVATIONLOG.txt'
csv_file = 'DBSS_SNOC_ACTIVATIONLOG.csv'

with open(dump_file, 'r', encoding="utf-8") as f:
    header = next(f).replace('\n','').split('|')
    lines = f.readlines()

with open(csv_file, 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    i = 0
    for line in lines:
        columns = line.split('|')
        writer.writerow(columns)

        i += 1
        print(f"completed {i}/{len(lines)}")