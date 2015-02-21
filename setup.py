from setuptools import setup


setup(
    name='Pyladies-Pastebin',
    py_modules=['pastebin'],
    install_requires=[
        'Flask',
        'Flask-OAuth',
        'Flask-SQLAlchemy',
    ]
)
