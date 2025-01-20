import csv
import io
from app.services.DB import DB

class Logs:
    def log(self, data):
        db = DB()
        cursor = db.getCursor()

        cursor.execute('insert into logs(operation, result) values (%s, %s)', (data['operation'], data['result']))
        db.commit()

    def dump(self):
        db = DB()
        cursor = db.getCursor(True)
        cursor.execute('select * from logs order by id desc')
        data = cursor.fetchall()

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(('id','operation','result'))
        for row in data:
            writer.writerow((row['id'], row['operation'], row['result']))

        output.seek(0)
        return output
