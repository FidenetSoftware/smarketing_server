from datetime import datetime
from sqlalchemy import func

#Calcular los porcentajes de los sentimientos 
def calculatePercentage(value):
    percentage_value = value * 100
    formatted_percentage = f"{percentage_value:.2f}%"
    return formatted_percentage;

#Convertir el objeto a un JSON
def convert_to_json(obj, fields):
    data = {}
    for field in fields:
        value = getattr(obj, field)
        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        data[field] = value
    return data

#Obtener la cuenta de los registros registrados 
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()])
    count = q.session.execute(count_q).scalar()
    return count