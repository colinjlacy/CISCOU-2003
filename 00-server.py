from flask import Flask

app = Flask(__name__)
f = open("./data/json-example.json")
data = f.read()
f.close()


@app.route('/')
def example():
    return data, 200


if __name__ == '__main__':
    app.run()
