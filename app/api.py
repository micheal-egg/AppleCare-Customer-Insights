import sqlite3
from flask import Flask, render_template, request, jsonify

# Creating Flask Application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True #Auto reloading like react, makes life easier

# ---- DB connection helper ----
def db():
    """
    Opens voc.db and returns a connection whose rows behave like dicts.
    Close it after each request.
    """
    con = sqlite3.connect("voc.db")
    con.row_factory = sqlite3.Row
    return con

# ---- Routes ----

# Home page
@app.get("/")  # When Home page is accessed, run below code
def home():    # Runs when home page is accessed
    return render_template("index.html")

# Health check
@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/search")
def search():
    q = (request.args.get("q", "") or "").lower()
    min_rating = int(request.args.get("min_rating", 1))
    month = (request.args.get("month") or "").strip()      # e.g., "2023-11"
    region = (request.args.get("region") or "").strip()    # e.g., "US", "EU", ...

    sql = [
        "SELECT survey_id, submitted_at, product_line, region, rating, comment_clean",
        "FROM surveys",
        "WHERE lower(comment_clean) LIKE ? AND rating >= ?"
    ]
    params = [f"%{q}%", min_rating]

    # filter by month (submitted_at is YYYY-MM-DD → take first 7 chars)
    if month:
        sql.append("AND substr(submitted_at,1,7) = ?")
        params.append(month)

    # filter by region
    if region and region.upper() != "ALL":
        sql.append("AND region = ?")
        params.append(region)

    sql.append("ORDER BY submitted_at DESC LIMIT 200;")
    sql = "\n".join(sql)

    con = db()
    try:
        rows = con.execute(sql, params).fetchall()
    finally:
        con.close()

    return jsonify([dict(r) for r in rows])
