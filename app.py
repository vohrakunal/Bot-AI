# Inbuild Functions
from flask import Flask, json, render_template, url_for, request
import collections


# Local Functions
from controller.jsoninput import convtoarr

app = Flask(__name__)


# HOME
@app.route("/")
def home():
      retnshowjson = convtoarr("assignment_1_input_1")
      return render_template("index.html", file=retnshowjson)

# VALUE REDIRECT
@app.route('/jsondata', methods=['POST'])
def get_names():
      outputarr = collections.OrderedDict()
      
      
      def createindex(stageval, optval):
            if stageval in outputarr:
                  if optval == 1:
                        outputarr[stageval]["Bot Says"]["message"]["quick_replies"] = {}
                  return
            else:
                  outputarr[stageval] = {}
                  outputarr[stageval]["Bot Says"] = {}
                  outputarr[stageval]["Bot Says"]["message"] = {}
                  outputarr[stageval]["Bot Says"]["message"]["text"] = {}

                  outputarr[stageval]["User Says"] = {}
                  if optval == 1:
                        outputarr[stageval]["Bot Says"]["message"]["quick_replies"] = {}
                  return

      # END OF createindex()


      if request.method == 'POST':
            names = request.json['data']
            
            stage = 0
         
            for stage in range(0,len(names)):
                  instvalue = "inst" + str(stage)
                  stagevalue = "stage" + str(stage)
                  textvalue = "text"+ str(stage)
                  inputvalue = "input"+ str(stage)
                  optionvalue = "option" + str(stage)
                  if instvalue in names:
                        createindex(stagevalue, 0)
                        outputarr[stagevalue]['Bot Says']['message']['text'] = names[instvalue]
                  if textvalue in names:
                        createindex(stagevalue, 0)
                        outputarr[stagevalue]['Bot Says']['message']['text'] = names[textvalue]
                  if inputvalue in names:
                        createindex(stagevalue, 0)
                        outputarr[stagevalue]['User Says'] = names[inputvalue]
                  if optionvalue in names:
                        createindex(stagevalue, 1)
                        outputarr[stagevalue]['Bot Says']['message']['quick_replies'] = names[optionvalue]
            
            jsonvalrtn = json.dumps(outputarr)
      
            print (jsonvalrtn)
            
                             
      return '', 200

if __name__ == "__main__":
      app.run(debug=True)
