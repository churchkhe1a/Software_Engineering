def register_visit(visit_record):
    name, surname, cabinet_number, time = visit_record.split()
    cabinet_number = int(cabinet_number)
    visit_log = {
        cabinet_number: [
            {
                "name": name,
                "surname": surname,
                "time": time
            }
        ]
    }
    return visit_log

visit_record = "Иван Иванов 101 14:30"
visit_log = register_visit(visit_record)
print(visit_log)
