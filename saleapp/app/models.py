from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Integer, default=0)
    image = Column(String(500), nullable=1)
    active = Column(Boolean, default=1)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        products = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://cdn.alloallo.media/catalog/product/apple/iphone/iphone-7-plus/iphone-7-plus-rose-gold.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://didongmango.com/images/products/2023/04/04/large/ipad-pro-11-inch-wifi-cellular-128gb-2020-bac-600x600-1-200x200_1680665788.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://cdn.tgdd.vn/Products/Images/42/206176/samsung-galaxy-note-10-plus-silver-new-400x400.jpg",
            "category_id": 1
        }, {
            "id": 4,
            "name": "Iphone 16 ProMax",
            "description": "Iphone, 256GB, RAML: 6GB",
            "price": 34990000,
            "image":
                "https://cdn.tgdd.vn/Products/Images/42/329149/s16/iphone-16-pro-max-titan-sa-mac-thumbnew-650x650.png",
            "category_id": 2
        }, {
            "id": 5,
            "name": "Iphone 16 Pro",
            "description": "Iphone, 128GB, RAML: 6GB",
            "price": 28990000,
            "image":
                "https://cdn.tgdd.vn/Products/Images/42/329143/iphone-16-pro-titan-tu-nhien.png",
            "category_id": 1
        }, {
            "id": 6,
            "name": "Iphone 16 Plus",
            "description": "Iphone, 128GB, RAML: 6GB",
            "price": 25990000,
            "image":
                "https://cdn.tgdd.vn/Products/Images/42/329138/iphone-16-plus-xanh-thumb-600x600.jpg",
            "category_id": 2
        }]

        for p in products:
            p = Product(**p)
            db.session.add(p)

        db.session.commit()
