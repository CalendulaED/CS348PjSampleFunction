from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    message = "cs348 project stage 2 sample function"
    return render_template("index.html", data = message)

@app.route('/func1')
def function1_page():
    f1Content = sampleFunction()
    return render_template("function_1.html", data=f1Content)

def sampleFunction():
    mydb = mysql.connector.connect(user='root', password='wgzzsql',
                                   host='104.197.213.149',
                                   database='wgzzdb')

    cursor = mydb.cursor()
    query = 'SELECT ShowName From ActIn Natural join Shows'
    cursor.execute(query)
    str = ""
    for line in cursor:
        for part in line:
            # substr = part.encode('ascii', 'ignore')
            # str = str + substr + ',' + ' '
            str = str + part + ', '
    cursor.close()
    mydb.close()
    return str

if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)
