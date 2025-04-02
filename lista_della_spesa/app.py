from flask import Flask, render_template #importiamo la classe flask
app = Flask(__name__) #inizializza app flask

@app.route('/') #decoratore per definire la route
def home():
    return render_template("index.html")



#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale