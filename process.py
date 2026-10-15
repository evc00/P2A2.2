
def process_grade(grade):
    if not isinstance(grade, (int, float)):
        return "Error: calificación inválida"

    if grade < 0 or grade > 100:
        return "Error: calificación fuera de rango"

    if grade >= 70:
        result = "Aprobado"
    else:
        result = "Reprobado"

    return result
