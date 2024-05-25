from django.shortcuts import render
from django.http import HttpResponse, JsonResponse    


import pandas as pd
import numpy as np

import psycopg2




def index(request):
    return HttpResponse("hello, world")


 
# test
# Create your views here.



def helloworld(request):
    # dates = pd.date_range('2022-01-01', '2022-01-10')
    # df = pd.DataFrame({
    #     'date': dates,
    #     'sales': np.round(np.random.rand(len(dates))*1000)
    # })
    # # table classes, if needed (ex: Bootstrap)
    # # classes=["table-bordered", "table-striped", "table-hover"]
    # table_data = df.to_html(table_id="table_example")
    # context = {'table_data': table_data}

    dbname = 'apt'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5432'

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    df = pd.read_sql("select * from apt_transactions", conn)

    context = {'table_data': df.to_html()}
    
    
    return render(request, "top100.html", context)




def getApt100(request):

    dbname = 'apt'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5432'

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    df = pd.read_sql("select * from apt_transactions", conn)

    context = {'table_data': df.to_html()}

    return JsonResponse(context)