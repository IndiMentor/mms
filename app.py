from flask import Flask, redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from ash.ashfile import ash_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="dfjhldsjlkdshfdy984y39h9h"
app.config['EXPLAIN_TEMPLATE_LOADING']=True
app.config['DEBUG']=True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)


    def __repr__(self):
        return '<User %r>' % self.username

class Escort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


    def __repr__(self):
        return '<Escort %r>' % self.name


admin = Admin(app, name='microblog', template_mode='bootstrap3',url="/")

# Add administrative views here
# @app.route("/")
# def index():
#     return redirect("/ad/")

class Preview(BaseView):
    @expose("/")
    def ad(self):
        return self.render("showad.html")

class Stats(BaseView):

    @expose("/")
    def lee(self):
        db.create_all()
        return self.render("lee.html",caller="root")
    @expose("/all")
    def all(self):
        return self.render("lee.html",caller="all")

class EscortView(ModelView):
    list_template = "escort_list.html"
    # @expose("/new/",methods=('GET','POST'))
    # def create_escort(self):
    #     return self.render("ce.html")

admin.add_view(Preview())
admin.add_view(Stats(url="/bob"))
admin.add_view(ModelView(User,db.session))
admin.add_view(EscortView(Escort,db.session))
app.register_blueprint(ash_bp)
app.run()
