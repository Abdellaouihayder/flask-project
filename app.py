from flask import Flask,request,jsonify
import products

pobj=products.Products()


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask! hayder content"

@app.route('/about')
def about():
    return "About Page"

@app.route('/products')
def productList():
    data=pobj.getProducts()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)  # Make sure debug mode is enabled
