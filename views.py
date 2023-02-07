from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key="a"
data=[]

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ajout')
def ajout():
    return render_template("ajout.html")
@app.route('/recherche')
def recherche():
    return render_template("recherche.html")
@app.route('/ajout_valider',methods=["POST", "GET"])
def ajout_valider():
    nom=request.form['nom_ajout']
    numero=request.form['numero_ajout']
    data.append((nom,numero))
    flash("Le numero de telephone " + numero + " a ete ajoute")
    return render_template("ajout_valide.html")
@app.route('/recherche_valider',methods=["POST", "GET"])
def recherche_valider():
    exist=False
    nom=request.form['nom_recherche']
    for i in data:
        if i[0]==nom:
            numero=i[1]
            exist=True
    if exist:
     flash("Nom : " + nom  + ", Numéro de téléphone : " + numero)
    else:
        flash("Désolé, le nom " + nom + " est inconnu")
    return render_template("recherche_valide.html")
    


app.run(debug=True)