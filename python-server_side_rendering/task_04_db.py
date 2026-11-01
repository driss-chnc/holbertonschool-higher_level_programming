from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            products_list = read_json()

        elif source == 'csv':
            products_list = read_csv()

        elif source == 'sql':
            products_list = read_sql()

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

    except (sqlite3.Error, OSError, json.JSONDecodeError, csv.Error):
        return render_template(
            'product_display.html',
            products=[],
            error="Database error"
        )


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
