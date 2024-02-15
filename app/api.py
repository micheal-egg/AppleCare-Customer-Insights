from flask import Flask, render_template

#Creating Flask Application
app = Flask(__name__)

# Defining Routes and Home Page
@app.get("/") #When Home page is accessed, run below code
def home(): #Runs when home page is accessed 
    return render_template("index.html")

#Checking API Health
@app.get("/api/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)