from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    
    
    return render_template('index.html')   


@app.route('/shop')
def shop():
    
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    
    return render_template('shop.html', items=items) 


# @app.route('/about/<username>')
# def about(username):
#     return f'<h1>This is about page of {username}</h1>'




if __name__ == '__main__':
    app.run(debug=True)