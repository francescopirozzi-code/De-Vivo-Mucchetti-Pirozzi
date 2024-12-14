from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from datetime import datetime
from database import db, Utente, Articolo, init_db, Carrello, Contiene
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'la_tua_chiave_segreta'

# Configura e inizializza il database
init_db(app)

PRODOTTO_DA_AGGIUNGERE = 'CAPERLAN - F/ROD - 45'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        mail = request.form['mail']
        nome = request.form['nome']
        cognome = request.form['cognome']
        data_di_nascita_str = request.form['data_di_nascita']
        password = generate_password_hash(request.form['password'])
        telefono = request.form['telefono']

        try:
            data_nascita = datetime.strptime(data_di_nascita_str, '%Y-%m-%d').date()
            # Controlla se l'utente esiste già
            utente_esistente = Utente.query.filter_by(mail=mail).first()
            if utente_esistente:
                flash('Email già registrata. Scegli un\'altra email.', 'error')
                return render_template('Sign_up_page.html')

            nuovo_utente = Utente(mail=mail, nome=nome, cognome=cognome, data_di_nascita=data_nascita, password=password, telefono=telefono)
            db.session.add(nuovo_utente)
            db.session.flush()  # Forza l'assegnazione dell'ID al nuovo utente

            # Crea un carrello per il nuovo utente
            nuovo_carrello = Carrello(id_carrello='CARRELLO_' + mail, mail_proprietario=mail)
            db.session.add(nuovo_carrello)
            db.session.flush() # Forza l'assegnazione dell'ID al nuovo carrello

            # Aggiungi il prodotto al carrello
            prodotto = Articolo.query.get(PRODOTTO_DA_AGGIUNGERE)
            if prodotto:
                contiene = Contiene(id_carrello=nuovo_carrello.id_carrello, nome_articolo=prodotto.nome_articolo, data_aggiunta=datetime.now())
                db.session.add(contiene)
            else:
                print(f"Prodotto {PRODOTTO_DA_AGGIUNGERE} non trovato.")

            db.session.commit()
            flash('Registrazione avvenuta con successo!', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()
            flash(f"Errore durante la registrazione: {e}", 'error')
            return render_template('Sign_up_page.html')

    return render_template('Sign_up_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('profilo'))
    else:
        return render_template('Log_in_page.html')

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Catalogo_page')
def Catalogo_page():
    return render_template('Catalogo_page.html')

@app.route('/AcquaSpectra')
def AcquaSpectra():
    return render_template('AcquaSpectra.html')

@app.route('/Carrello')
def Carrello():
    return render_template('Carrello.html')

@app.route('/Chi_siamo')
def Chi_siamo():
    return render_template('Chi_siamo.html')

@app.route('/Contatti')
def Contatti():
    return render_template('Contatti.html')

@app.route('/Contenitore_da_pesca')
def Contenitore_da_pesca():
    return render_template('Contenitore_da_pesca.html')

@app.route('/F_ROD_35')
def F_ROD_35():
    return render_template('F_ROD_35.html')

@app.route('/F_ROD_45')
def F_ROD_45():
    return render_template('F_ROD_45.html')

@app.route('/Guadino_da_pesca')
def Guadino_da_pesca():
    return render_template('Guadino_da_pesca.html')

@app.route('/Moran')
def Moran():
    return render_template('Moran.html')

@app.route('/Moran_five')
def Moran_five():
    return render_template('Moran_five.html')

@app.route('/Nautica2026')
def Nautica2026():
    return render_template('Nautica2026.html')

@app.route('/Pinne_belly')
def Pinne_belly():
    return render_template('Pinne_belly.html')

@app.route('/Rot_50_47')
def Rot_50_47():
    return render_template('Rot_50_47.html')

@app.route('/Sacca_da_pesca')
def Sacca_da_pesca():
    return render_template('Sacca_da_pesca.html')

@app.route('/Sedia_pieghevole_da_pesca')
def Sedia_pieghevole_da_pesca():
    return render_template('Sedia_pieghevole_da_pesca.html')

@app.route('/Stivali_40_57')
def Stivali_40_57():
    return render_template('Stivali_40_57.html')

@app.route('/SubSuit')
def SubSuit():
    return render_template('SubSuit.html')

@app.route('/SubSuit2')
def SubSuit2():
    return render_template('SubSuit2.html')

@app.route('/User_page')
def User_page():
    return render_template('User_page.html')

@app.route('/Waders_da_pesca')
def Waders_da_pesca():
    return render_template('Waders_da_pesca.html')

@app.route('/Log_in_page')
def Log_in_page():
    return render_template('Log_in_page.html')

@app.route('/Sign_up_page')
def Sign_up_page():
    return render_template('Sign_up_page.html')

# Route temporanea per la pagina del profilo
@app.route('/profilo')
def profilo():
    return "User_page.html"

def insert_test_data():
    if not Utente.query.first():
        crea_utente = Utente(mail='luigi.scafandri@gmail.com', nome='Luigi', cognome='Scafandri', data_di_nascita=datetime.strptime('1979-11-30', '%Y-%m-%d').date(), password=generate_password_hash('Gigi3540'), telefono='3334567764')
        crea_utente2 = Utente(mail='gregorioarmeno@gmail.com', nome='Gregorio', cognome='Armeno', data_di_nascita=datetime.strptime('1969-10-12', '%Y-%m-%d').date(), password=generate_password_hash('Greg6996'), telefono='3334452378')
        crea_utente3 = Utente(mail='lino.fareone50@hotmail.com', nome='Lino', cognome='Faraone', data_di_nascita=datetime.strptime('1978-11-12', '%Y-%m-%d').date(), password=generate_password_hash('Egypt507'), telefono='3226763779')
        crea_utente4 = Utente(mail='davide.parton@outlook.it', nome='Davide', cognome='Patron', data_di_nascita=datetime.strptime('1988-07-03', '%Y-%m-%d').date(), password=generate_password_hash('David88'), telefono='3667778940')
        db.session.add_all([crea_utente, crea_utente2, crea_utente3, crea_utente4])

        crea_articolo1 = Articolo(nome_articolo='MIKADO - Waders da pesca', prezzo=130, numero_pezzi_disponibili=50)
        crea_articolo2 = Articolo(nome_articolo='CAPERLAN - Stivali 40/57', prezzo=55, numero_pezzi_disponibili=50)
        crea_articolo3 = Articolo(nome_articolo='CAPERLAN - Pinne belly - boat pesca artificiali FLTBFI+', prezzo=58.90, numero_pezzi_disponibili=50)
        crea_articolo4 = Articolo(nome_articolo='CAPERLAN - Sacca da pesca', prezzo=35, numero_pezzi_disponibili=50)
        crea_articolo5 = Articolo(nome_articolo='CAPERLAN - F/ROD - 35', prezzo=45, numero_pezzi_disponibili=150)
        crea_articolo6 = Articolo(nome_articolo='MORAN - Frida', prezzo=900000.00, numero_pezzi_disponibili=30)
        crea_articolo7 = Articolo(nome_articolo='MORAN - Five Waves', prezzo=5922800.00, numero_pezzi_disponibili=30)
        crea_articolo8 = Articolo(nome_articolo='CAPERLAN - Sedia pieghevole da pesca', prezzo=95, numero_pezzi_disponibili=75)
        crea_articolo9 = Articolo(nome_articolo='CAPERLAN - Guadino da pesca', prezzo=25.60, numero_pezzi_disponibili=50)
        crea_articolo10 = Articolo(nome_articolo='CAPERLAN - Contenitore da pesca', prezzo=57.90, numero_pezzi_disponibili=50)
        crea_articolo11 = Articolo(nome_articolo='CAPERLAN - SubSuit/006', prezzo=75, numero_pezzi_disponibili=50)
        crea_articolo12 = Articolo(nome_articolo='GHOTA - AcquaSpectra Ultra', prezzo=4500, numero_pezzi_disponibili=50)
        crea_articolo13 = Articolo(nome_articolo='CAPERLAN - F/ROD - 45', prezzo=150, numero_pezzi_disponibili=50)
        crea_articolo14 = Articolo(nome_articolo='CAPERLAN - Rot/5047', prezzo=65, numero_pezzi_disponibili=50)
        crea_articolo15 = Articolo(nome_articolo='CAPERLAN - SubSuit/007', prezzo=75, numero_pezzi_disponibili=90)
        db.session.add_all([crea_articolo1, crea_articolo2, crea_articolo3, crea_articolo4, crea_articolo5, crea_articolo6, crea_articolo7, crea_articolo8, crea_articolo9, crea_articolo10, crea_articolo11, crea_articolo12, crea_articolo13, crea_articolo14, crea_articolo15])

        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        insert_test_data()
    app.run(debug=True)