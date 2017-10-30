from . import app
import datetime
from flask import request
from flask import render_template


@app.route('/', methods=['GET'])
def index():

    TitleName = "Day of the Week Calculator"
    HeadName = "Day of the Week Calculator"

    userinput = request.args.get('userdate', 0)

    
