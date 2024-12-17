from flask import Flask, render_template, request, redirect, url_for, session
import database as db
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your secret key'  # Change this!

# Check if database is empty and populate
if not db.get_all_products():
    db.add_products_test()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if password != password_confirm:
          return render_template('register.html', error='Le password non corrispondono.')
        if db.get_user_by_username(username):
          return render_template('register.html', error='Username già in uso.')
        db.register_user(username, password, email)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.get_user_by_username(username)
        if user and db.verify_password(password, user['password_hash']):
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        return render_template('login.html', error='Credenziali non valide.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
  user = db.get_user_by_id(session['user_id'])
  return render_template('dashboard.html', user=user)

@app.route('/User_page')
@login_required
def user_page():
    user = db.get_user_by_id(session['user_id'])
    return render_template('User_page.html', user=user)

@app.route('/Catalogo_page')
def catalog_page():
    products = db.get_all_products()
    return render_template('Catalogo_page.html', products = products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    quantity = request.form.get('quantity', 1, type=int)
    db.add_item_to_cart(session['user_id'], product_id, quantity)
    return redirect(url_for('catalog_page'))

@app.route('/Carrello')
@login_required
def cart_page():
    cart_items = db.get_cart_items_by_user(session['user_id'])
    return render_template('Carrello.html', cart_items=cart_items)

@app.route('/remove_from_cart/<int:cart_item_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_item_id):
    db.remove_cart_item(cart_item_id)
    return redirect(url_for('cart_page'))

@app.route('/update_cart_quantity/<int:cart_item_id>', methods=['POST'])
@login_required
def update_cart_quantity(cart_item_id):
   quantity = request.form.get('quantity', type=int)
   db.update_cart_item_quantity(cart_item_id, quantity)
   return redirect(url_for('cart_page'))

@app.route('/AcquaSpectra_details')
def acqua_spectra_details():
    product = db.get_product_by_name("Acqua Spectra")
    return render_template('AcquaSpectra_details.html', product = product)

@app.route('/Nautica2026')
def nautica_2026():
    return render_template('Nautica2026.html')

@app.route('/Chi_siamo')
def chi_siamo():
    return render_template('Chi_siamo.html')

@app.route('/Contatti')
def contatti():
    return render_template('Contatti.html')


if __name__ == '__main__':
    app.run(debug=True)