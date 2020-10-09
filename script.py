import pandas as pd
import csv

from budgets.models import Lancamento

def run():
    # 1. Read database.
    fhand = open('csv/customer_new.csv')
    reader = csv.reader(fhand)

    # 7. Delete all customer table objects
    Lancamento.objects.all().delete()
    
    for row in reader:
        p, created = Lancamento.objects.get_or_create(lancamento=row[0], first_name=row[1], last_name=row[2], email=row[3],
                                                         gender=row[4], company=row[5], city=row[6],
                                                         title=row[7], lat=row[8], lon=row[9])
    print('')
    print("Load complete! Open http://localhost:8000")
