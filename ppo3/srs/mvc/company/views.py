from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from company.utils import make_date


@api_view(['GET'])
def get_payroll_data(request):
    employee_id = request.query_params.get('employee_id')

    month = request.query_params.get('month')
    year = request.query_params.get('year')
    date = make_date(year, month)
    cursor = connection.cursor()
    cursor.execute(f'''
            EXEC payroll_data @employee_id={employee_id}, @date_="{date}"
            ''')
    result = cursor.fetchone()
    data = {}
    if result:
        data = {
            "salary": result[0],
            "production_count": result[1],
            "sale_count": result[2],
            "purchase_count": result[3],
            "prize_percent": result[4],
            "summary": result[1] + result[2] + result[3],
        }
        data['prize'] = data['summary'] * ((data['salary'] * data['prize_percent']) / 100)
        data['total'] = data['salary'] + data['prize']
    cursor.close()
    return Response(data)

