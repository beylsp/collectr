from sqlalchemy import Integer, Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SparkModelData(Base):
    __tablename__ = 'sparkmodel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String(8), unique=True)
    image_url = Column(String(1000))
    title = Column(String(1000))
    in_collection = Column(Integer, default=0)

    def __init__(self, product_id=None, image_url=None,
                 title=None, in_collection=0):
        self.product_id = product_id
        self.image_url = image_url
        self.title = title
        self.in_collection = in_collection

    def __repr__(self):
        return "<SparkModelData: product_id='%s', image_url='%s', "
        "title='%s', in_collection='%s'>" % (
            self.product_id, self.image_url, self.title, self.in_collection)
