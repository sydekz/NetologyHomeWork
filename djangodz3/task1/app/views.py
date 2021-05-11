from django.shortcuts import render
import csv

CSV_FILE_NAME = 'inflation_russia.csv'


def read_csv_file(csvfile):
    context = list()

    with open(csvfile, "r", encoding='utf8') as f_obj:
        reader = csv.reader(f_obj, delimiter=';')
        name_list = next(reader)
        for row in reader:
            print(row[0])
            context.append({'Jan': row[1], 'Feb': row[2], 'Mar': row[3], 'Apr': row[4], 'May': row[5], 'Jun': row[6],
                            'Jul': row[7], 'Aug': row[8], 'Sep': row[9], 'Oct': row[10], 'Nov': row[11],
                            'Dec': row[12], 'Months': row[1:-1], 'Year': row[0], 'Sum': row[-1]})

    return context, name_list


def inflation_view(request):
    template_name = 'inflation.html'
    data, names = read_csv_file(CSV_FILE_NAME)
    # чтение csv-файла и заполнение контекста
    context = {'data': data, 'names': names}

    return render(request, template_name, context)