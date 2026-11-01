from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json()

    elif source == 'csv':
        products_list = read_csv()

    else:
        return render_template(
            'product_display.html',
            products=[],
            error="Wrong source"
        )

    if product_id:
        products_list = [
            product for product in products_list
            if str(product['id']) == product_id
        ]

        if not products_list:
            return render_template(
                'product_display.html',
                products=[],
                error="Product not found"
            )

    return render_template(
        'product_display.html',
        products=products_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
