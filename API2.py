#  QUES : Make a simple project using Flask and perform get and post method .

from flask import Flask , jsonify , request

app = Flask(__name__)

data = [
    {
        "id":1,
         "Name":"Annu Dhull",
         "Age":22 , 
         " Course":"MCA",
         "Company Name":"CloudEQ"

    },
    {
        "id":2,
        "Name":"Shivani",
         "Age":19 , 
         "Course":"Bcom",
         "Company Name" : "CloudEQ"
    }
]

@app.route("/")

def Nature_is_Beautiful():
    return "**** Nature is like a HEAVEN ****"

@app.route("/add-data1",methods = ["POST"])
def add_data():
    
    data1 = 
        {

        "id":data1[-1]['id'] + 1,
         "Name":request.json["Name"],
         "Age":request.json["Age"], 
         "Course":request.json["Course"],
         "Company Name" : request.json["Company Name"]
        }
    
    data.append(data1)
    return jsonify({
        "status":"success",
        "message":"added sucesfully"
    })
@app.route("/get-data")
def get_data():
    return jsonify({
        "info" ="data1"
    })

if (__name__=="__main__"):
    app.run(debug=True)
# -----------------------------------------------------------------------------------------------------------------------------

