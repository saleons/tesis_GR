from flask import Flask,render_template,request,redirect
import ee
from flask_sqlalchemy import SQLAlchemy




# importo la libreria ee de eart engine
import ee
service_account = 'saleons@unincca.edu.co'
# registro de usuario de google eart
credentials = ee.ServiceAccountCredentials(service_account, 'leafy-rope-354103-63997f0b87b4.json')
# uno el .json que descargue de google cloud
ee.Initialize(credentials)
# se envian datos para entra
import folium

# aqui le paso las coordenadas al mapa principal
mapaobjeto = folium.Map(location=[6.1236, -75.6750])
# actualice el mapa
iframe = mapaobjeto._repr_html_()

# se le asigna el codigo html
#mapaobjeto.get_root().html.add_child(folium.Element("""

#<head>
#	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min-.js"></script>
#</head>
#"""))


# guardo mapa
#mapaobjeto.save("templates/index.html")


#img = ee.Image('LANDSAT/LT05/C01/T1_SR/LT05_034033_20000913')
# ene le objeto iamgen se guarda la iamgen landsat

#print(img)

# Print image object WITH call to getInfo(); prints image metadata.
#print(img.getInfo())


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/muestra'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class nivel_confianza(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Nivel=db.Column(db.Numeric(100))
    Z=db.Column(db.Numeric(100))


@app.route('/')
def index():
     d=[]
     tasks=nivel_confianza.query.all()
     for tar in tasks:
             d.append(tar.Z)
            
     return render_template("index.html",d=d)   

@app.route('/RESULTADO',methods=['POST'] )
def a():
     if request.method =="POST": 
         N=float(request.form["N"])
         Z=float(request.form["Z"])
         Z=Z**2
         e=int(request.form["e"])
         e=e/100
         p=int(request.form["p"])
         p=p/100
         q=int(request.form["q"])
         q=q/100
         print(N)
         print(Z)
         print(e)
         print(p)
         print(q)
        
         resultado=(p*q*Z)/e**2
         print(resultado)
         d=[]
         tasks=nivel_confianza.query.all()
         for tar in tasks:
             d.append(tar.Z)
         return render_template("index.html",resultado=resultado,d=d)
        # al instancia redirect logro devolver al index


if __name__ == "__main__":
    app.run(debug=True, port=5000)


