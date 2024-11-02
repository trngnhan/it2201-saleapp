from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    prod = dao.load_product(cate_id=cate_id, kw=kw)
    return render_template('index.html', categories=cates, products=prod)


if __name__ == '__main__':
    app.run(debug=True)
