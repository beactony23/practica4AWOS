from flask import Flask, render_template, request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/respuestas')
def productos():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005037_usr",
        password="N&2lbK=8;Mrt",
        database="u760464709_24005037_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Respuesta")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

@app.route('/respuesta')
def producto():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005037_usr",
        password="N&2lbK=8;Mrt",
        database="u760464709_24005037_bd"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO Respuesta (Respuesta, idPregunta) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()
    return make_response(jsonify(myresult))

