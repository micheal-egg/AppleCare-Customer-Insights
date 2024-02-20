import sqlite3
from flask import Flask, render_template, request, jsonify

# Creating Flask Application
app = Flask(__name__)

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

# Search API: /api/search?q=activation&min_rating=2
@app.get("/api/search")
def search():
    # Read query params with defaults
    q = (request.args.get("q", "") or "").lower()
    min_rating = int(request.args.get("min_rating", 1))

    # Query SQLite
    con = db()
    try:
        rows = con.execute(
            """
            SELECT survey_id, submitted_at, product_line, region, rating, comment_clean
            FROM surveys
            WHERE lower(comment_clean) LIKE ? AND rating >= ?
            ORDER BY submitted_at DESC
            LIMIT 200;
            """,
            (f"%{q}%", min_rating),
        ).fetchall()
    finally:
        con.close()

    # Convert rows → JSON
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True)
