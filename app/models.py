from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Roles(db.Model):
    """class represents roles table"""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))


class Permissions(db.Model):
    """class represents permissions table"""
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key = True)
    module = db.Column(db.String(60))
    activity = db.Column(db.String(60))


class Users(db.Model):
    """Class represents the users table"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    role = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default= db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp(),
                              onupdate = db.func.current_timestamp())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read password')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)

    @staticmethod
    def get_all():
        return Users.query.all()

    def __repr__(self):
        return "<User %r>" % format(self.name)

    class Shops(db.Model):
        """Class represents the shops table"""
        __tablename__ = 'shops'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        name = db.Column(db.String(60))
        email = db.Column(db.String(60))
        telephone = db.Column(db.String(60))
        description = db.Column(db.String(300))
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
        date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                  onupdate=db.func.current_timestamp())

    class Products(db.Model):
        """Class represents the products table"""
        __tablename__ = 'products'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(60))
        description = db.Column(db.String(60))
        price = db.Column(db.Float(2))
        quantity = db.Column(db.Float(2))
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
        date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                  onupdate=db.func.current_timestamp())

    class Attributes(db.Model):
        """Class captures attributes such as color, size"""
        __tablename__ = 'attributes'
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.Integer)
        name = db.Column(db.String(60))
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
        date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                  onupdate=db.func.current_timestamp())

    class ProductVariations(db.Model):
        """Class captures variations in product attributes"""
        __tablename__ = 'variations'
        id = db.Column(db.Integer, primary_key=True)
        attribute_id = db.Column(db.Integer, db.ForeignKey('attributes.id'))
        product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
        value = db.Column(db.String(60))
        price = db.Column(db.Float(2))
        quantity = db.Column(db.Float(2))
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
        date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                  onupdate=db.func.current_timestamp())