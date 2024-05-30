from lightapi import LightApi
from models.example_models import Person, Company

# class Person(CustomBase):
#     pk = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     name = Column(String)
#     email = Column(String, unique=True)
#
#
# class Company(CustomBase):
#     pk = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     name = Column(String)
#     email = Column(String, unique=True)


if __name__ == '__main__':
    app = LightApi()
    app.register({'/person': Person})
    app.register({'/company': Company})
    app.run()
