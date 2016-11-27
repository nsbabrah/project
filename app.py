

import os
from flask import Flask,render_template


app = Flask(__name__)
@app.route('/')
def navjotbabrah():
    return render_template("index.html")



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
