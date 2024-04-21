from flask import Flask , render_template, request

import requests   ## if you didnt find any of flask or request than bash and uniinstallll it

app = Flask(__name__)

@app.route('/')     #route what and where it should moves or id

def homepage():
    return render_template("index.html")   # location where to moove if this is true

@app.route("/weatherapp",methods = ['POST' , "GET"])    #post is secure method
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
#param ---- parameter or variavle
    param = {                                                       
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)   
    data = response.json()
    return f"data : {data}"

if __name__ == '__main__':       #main function
    app.run(host= "0.0.0.0" , port = 5002)

#push my code from local to git then to cloud



#after complititing this project you need to use various thinkgs in terminal to push it itno giti
#after this you need to add files like >>>>> git add . (for all the files)