from flask import Flask,request,jsonify
from flask_cors import cross_origin
import products

pobj=products.Products()


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask! hayder content"

@app.route('/about')
def about():
    return "About Page"

@app.route('/products',methods=['GET','POST'])
@cross_origin(origins="*",headers=['content-type'])
def productList():
    if(request.method=='GET'):
        data=pobj.getProducts()
        if len(data):
            response=jsonify({
                "resultat":data,
                "status":200
                })
        else:
            response=jsonify({
                "resultat":data,
                "status":400
                })
        return response
    elif(request.method=='POST'):
        data=request.json
        aData=pobj.createProduct(data)
        if(aData==200):
            response=jsonify({
                "resultat":aData,
                "status":200,
                "message":"created successfully"
            })
        else:
            response=jsonify({
                "resultat":aData,
                "status":400,
                "message":"failed of creation"})
                
        return response
#update data or delete using this url
@app.route('/product/<int:pid>',methods=['GET','PUT','DELETE','PATCH','OPTIONS'])
@cross_origin(origins="*",headers=['content-type'])
def productchange(pid):
    if(request.method=='PUT'):
        data=request.json
        aData=pobj.updateProduct(data,pid)
        if(aData==200):
            reponse=jsonify({
                "result":aData,
                "status":200,
                "message":"updated Successfully"
            })
        else:
            reponse=jsonify({
                "result":aData,
                "status":400,
                "message":"Failed to update"
            })
        return reponse
    elif(request.method=='DELETE'):
        aData=pobj.deleteProduct(pid)
        if(aData==200):
            reponse=jsonify({
            "result":aData,
            "status":200,
            "message":"Delete Successfully"
            })
        else:
            reponse=jsonify({
            "result":aData,
            "status":400,
            "message":"Failed to delete"
            })
        return reponse

    elif(request.method=='PATCH'):
        return "Patch http method"
    elif(request.method=='GET'):
        return "request to get single product"
    else:
        return("options http method")
    return reponse


if __name__ == "__main__":
    app.run(debug=True)  
