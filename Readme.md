# Bot-AI
*@vohrakunal*
> ver 1.0

### Requirements
- Python3
`# apt install python3`

- Flask
`# pip3 install flask`


Note: Please Install a virtual environment if required
`# apt install python3-venv`




------------


##### To Change Input JSON File: 
- In app.py file replace assignment_1_input_1 with some other file name in home() function and add the json file to /static/data folder 
    
       @app.route("/")
        def home():
              retnshowjson = convtoarr("assignment_1_input_1")
              return render_template("index.html", file=retnshowjson)
			  

