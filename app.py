from flask import Flask, request, jsonify
from db import connect

app = Flask(__name__)

# @app.route("/logs")
# def get_logs():
#     conn = connect()
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM logs")
#     rows = cur.fetchall()

#     cur.close()
#     conn.close()

#     return jsonify(rows)

@app.route("/logs")
def get_logs():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    offset = (page - 1) * limit

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM logs ORDER BY timestamp DESC LIMIT %s OFFSET %s",
        (limit, offset)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    # return jsonify(rows)
    result = []
    for row in rows:
        result.append({
           "id": row[0],
           "timestamp": str(row[1]),
           "level": row[2],
           "message": row[3]
    })

    return jsonify(result)


@app.route("/search")
def search_logs():
    keyword = request.args.get("keyword")
    level = request.args.get("level")
    start = request.args.get("start")
    end = request.args.get("end")

    conn = connect()
    cur = conn.cursor()

    query = "SELECT * FROM logs WHERE 1=1"
    params = []

    if keyword:
        query += " AND to_tsvector('english', message) @@ plainto_tsquery(%s)"
        params.append(keyword)

    if level:
        query += " AND level = %s"
        params.append(level)
    
    if start:
        query += " AND timestamp >= %s"
        params.append(start)

    if end:
        query += " AND timestamp <= %s"
        params.append(end)

    cur.execute(query, params)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    # return jsonify(rows)
    result = []
    for row in rows:
        result.append({
           "id": row[0],
           "timestamp": str(row[1]),
           "level": row[2],
           "message": row[3]
    })

    return jsonify(result)

@app.route("/")
def home():
    return "Log Analytics API Running"


app.run(debug=True)