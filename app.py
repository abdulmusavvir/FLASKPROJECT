from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@database-1.cbkcwsemeqb8.us-east-1.rds.amazonaws.com:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class currency(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    INR = db.Column(db.Float, nullable=False)
    USD = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<currency {self.id},{self.INR},{self.USD}>'

def create_tables():
    db.create_all()


@app.route("/", methods=['GET','POST'])
def home():
    INRValue = None
    USDValue = None
    if request.method == 'POST':
        INRValue= request.form.get('INR')
        if not INRValue:
            return 'INR Value is required!', 400
        USDValue = float(INRValue)*0.012
        USDValue =round(USDValue, 2)
        data = currency(INR=INRValue,USD=USDValue)
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e), 400
    return render_template('home.html', USDValue=USDValue,INRValue=INRValue)

@app.route("/result")
def result():
    results = currency.query.all()
    return render_template('result.html',results=results)

if __name__ == "__main__":
    app.run(debug=True,port=8096)