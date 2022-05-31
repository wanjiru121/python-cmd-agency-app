import csv

def write_to_csv():
    fields = []
    rows = []

    with open('real_estate.csv', 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    with open('real_estate_output.csv', 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(fields)
        writer.writerows(rows)
        output_file.close()
