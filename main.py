import mysql.connector
from flask import Flask, request

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="hiro",
  database="project_1"
)

@app.route("/insert", methods=['GET'])
def hello_world():
    args = request.args
    temperature = args.get("temperature")
    humidity = args.get("humidity")
    mycursor = mydb.cursor()
    sql = "INSERT INTO Records (temperature, humidity) VALUES ("+temperature+", "+humidity+")"
    mycursor.execute(sql)
    mydb.commit()
    return "<b>Record inserted "+str(mycursor.rowcount)+"</b>"

@app.route("/latest", methods=['GET'])
def latest_record():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Records ORDER BY id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    x = myresult[0]
    result = ""
    result += "Temperature: "+str(x[1])+" Celcius<br>"
    result += "Humidity: "+str(x[2])+"%"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)