from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    logging.info("we are testing logging module once again")
    return "CI CD pipeline established"

if __name__=="__main__":
    app.run(debug=True)