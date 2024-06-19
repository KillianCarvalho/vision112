from flask_cors import CORS
from flask import Flask, request, jsonify
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from datetime import datetime

app = Flask(__name__)

def execute_query_with_filters(type_alerte, vehicule_implique, date_debut, date_fin):
    cluster = Cluster(['localhost'], port=9042)
    session = cluster.connect('vision112')

    query = "SELECT * FROM fiche_accident WHERE accident_date_time >= %s AND accident_date_time <= %s"
    params = [date_debut, date_fin]



    if type_alerte and len(type_alerte) > 0 and type_alerte[0] != '':
        query += " AND type_alerte IN ({})".format(','.join(['%s'] * len(type_alerte)))
        params.extend(type_alerte)

    if vehicule_implique and len(vehicule_implique) > 0 and vehicule_implique[0] != '':
        query += " AND type_vehicule IN ({})".format(','.join(['%s'] * len(vehicule_implique)))
        params.extend(vehicule_implique)

    query += " ALLOW FILTERING"

    statement = SimpleStatement(query)
    result = session.execute(statement, params)

    return result

@app.route('/query')
def query():
    type_alerte = request.args.get('type_alerte')
    vehicule_implique = request.args.get('vehicule_implique')
    date_debut = request.args.get('date_debut')
    date_fin = request.args.get('date_fin')
    type_alerte = type_alerte.split(',')
    vehicule_implique = vehicule_implique.split(',')

    date_debut = datetime.fromisoformat(date_debut)
    date_fin = datetime.fromisoformat(date_fin)

    results = execute_query_with_filters(type_alerte, vehicule_implique, date_debut, date_fin)

    json_results = [{'uuid': row.uuid, 'event_date_time': row.event_date_time, 'source': row.source,
                     'type_data': row.type_data, 'coordonnee_lat': row.coordonnee_lat,
                     'coordonnee_long': row.coordonnee_long, 'code_postal': row.code_postal,
                     'type_alerte': row.type_alerte, 'type_vehicule': row.type_vehicule,
                     'accident_date_time': row.accident_date_time} for row in results]

    return jsonify(json_results)

if __name__ == "__main__":
    CORS(app)
    app.run(debug=True, port=5000)
