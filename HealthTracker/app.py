from flask import Flask, render_template, request, redirect, url_for
from database import DBManager  # Line 2: DBManager Class ko import kiya (OOP Concept)

app = Flask(__name__)

# --- OOP Line 7: Object Instantiation ---
# Yahan humne DBManager class ka ek 'Object' banaya hai.
# Ab saara database ka kaam isi 'db' object ke through hoga.
db = DBManager()

@app.route('/')
def dashboard():
    # --- OOP Line 14: Method Calling (Abstraction) ---
    # App ko nahi pata SQL query kya hai, wo sirf method call kar raha hai.
    user = db.get_user()
    
    if not user:
        return redirect(url_for('login_page'))
    
    # Aaj ka data fetch karne ke liye object ko call kiya
    stats = db.get_today_stats()

    # AI BMI Logic (Encapsulated in Controller)
    # user[2] is weight, user[3] is height
    bmi = round(user[2] / (user[3] * user[3]), 1)
    status = "Fit" if 18.5 <= bmi <= 24.9 else "Action Needed"

    # Smart Reminders Logic
    reminders = []
    if stats['steps'] < user[4]: # user[4] is Daily Goal
        reminders.append(f"Goal alert: {user[4] - stats['steps']} steps remaining!")
    if stats['water'] < 2000:
        reminders.append("Hydration alert: Drink more water!")

    return render_template('index.html', user=user, stats=stats, bmi=bmi, status=status, reminders=reminders)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/setup', methods=['POST'])
def setup():
    # --- OOP Line 45: Delegation ---
    # Controller ne data liya aur Object (db) ko bola ki isse save kar do.
    db.add_user(
        request.form.get('name'),
        request.form.get('age'),
        float(request.form.get('weight')),
        float(request.form.get('height')),
        int(request.form.get('goals'))
    )
    return redirect(url_for('dashboard'))

@app.route('/sync', methods=['POST'])
def sync():
    # --- OOP Line 58: Message Passing ---
    # User input ko database object ke method 'sync_data' mein pass kiya.
    steps = request.form.get('steps')
    water = request.form.get('water')
    db.sync_data(steps, water)
    return redirect(url_for('dashboard'))

@app.route('/report')
def report_page():
    # Final Report ke liye data mangwaya
    report_data = db.get_full_report()
    return render_template('report.html', 
                           user=report_data['user'], 
                           total_steps=report_data['steps'], 
                           total_cals=report_data['cals'], 
                           total_water=report_data['water'])

if __name__ == '__main__':
    app.run(debug=True)