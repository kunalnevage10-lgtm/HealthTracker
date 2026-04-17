import sqlite3

class DBManager:
    def __init__(self, db_name='healthsync.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS USER 
                          (UserID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           Name TEXT, Age INTEGER, Weight REAL, Height REAL, Daily_Goals INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS ACTIVITY_LOG 
                          (LogID INTEGER PRIMARY KEY AUTOINCREMENT, Step_Count INTEGER, 
                           Date TEXT, Calories_Burned REAL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS HYDRATION_LOG 
                          (WaterID INTEGER PRIMARY KEY AUTOINCREMENT, Amount_ML INTEGER, 
                           Timestamp TEXT)''')
        conn.commit()
        conn.close()

    def add_user(self, name, age, weight, height, goals):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER (Name, Age, Weight, Height, Daily_Goals) VALUES (?, ?, ?, ?, ?)", 
                       (name, age, weight, height, goals))
        conn.commit()
        conn.close()

    def get_user(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Age, Weight, Height, Daily_Goals FROM USER LIMIT 1")
        user = cursor.fetchone()
        conn.close()
        return user

    def sync_data(self, steps, water):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if steps and steps != "":
            cals = int(steps) * 0.04
            cursor.execute("INSERT INTO ACTIVITY_LOG (Step_Count, Date, Calories_Burned) VALUES (?, date('now'), ?)", (steps, cals))
        if water and water != "":
            ml = int(water) * 250
            cursor.execute("INSERT INTO HYDRATION_LOG (Amount_ML, Timestamp) VALUES (?, datetime('now'))", (ml,))
        conn.commit()
        conn.close()

    # --- YEH WOH MISSING METHOD HAI JISSE ERROR AA RAHA THA ---
    def get_today_stats(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Step_Count), SUM(Calories_Burned) FROM ACTIVITY_LOG WHERE Date = date('now')")
        steps_data = cursor.fetchone()
        cursor.execute("SELECT SUM(Amount_ML) FROM HYDRATION_LOG WHERE date(Timestamp) = date('now')")
        water_data = cursor.fetchone()
        conn.close()
        return {
            "steps": steps_data[0] or 0,
            "cals": round(steps_data[1] or 0, 2),
            "water": water_data[0] or 0
        }

    # --- REPORT KE LIYE METHOD ---
    def get_full_report(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Age, Weight, Height FROM USER LIMIT 1")
        user = cursor.fetchone()
        cursor.execute("SELECT SUM(Step_Count), SUM(Calories_Burned) FROM ACTIVITY_LOG")
        act = cursor.fetchone()
        cursor.execute("SELECT SUM(Amount_ML) FROM HYDRATION_LOG")
        wat = cursor.fetchone()
        conn.close()
        return {
            "user": user,
            "steps": act[0] or 0,
            "cals": round(act[1] or 0, 2),
            "water": wat[0] or 0
        }