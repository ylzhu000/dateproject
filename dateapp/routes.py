from . import app
import datetime
from flask import request
from flask import render_template


@app.route('/', methods=['GET'])
def index():

    TitleName = "Day of the Week Calculator"
    HeadName = "Day of the Week Calculator"

    userinput = request.args.get('userdate', 0)

    if userinput:
      InputYear, InputMonth, InputDay = (int(x) for x in str(userinput).split('-'))
      Input_weekday = datetime.date(InputYear, InputMonth, InputDay).weekday()
      if Input_weekday == 0:
           Input_weekday = "Monday"
      elif Input_weekday == 1:
           Input_weekday = "Tudesday"
      elif Input_weekday == 2:
           Input_weekday = "Wednesday"
      elif Input_weekday == 3:
           Input_weekday = "Thursday"
      elif Input_weekday == 4:
           Input_weekday = "Friday"
      elif Input_weekday == 5:
           Input_weekday = "Saturday"
      else:
           Input_weekday = "Sunday"

      return render_template("index.html", TitleName = TitleName, HeadName = HeadName,
      Input_weekday = Input_weekday, InputYear = InputYear, InputMonth = InputMonth, InputDay = InputDay)

    else:
       return render_template("index.html", TitleName = TitleName, HeadName = HeadName)
