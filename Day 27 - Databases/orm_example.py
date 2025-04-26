from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///orm.db')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add product
new_product = Product(name="Laptop", price=999, quantity=5)
session.add(new_product)
session.commit()

# Query products
print("All products:", session.query(Product).all())