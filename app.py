from flask import Flask
from flask import render_template
app = Flask(__name__)

#/ is the homepage of our website. 
# With this one line of code, we are pointing this code to our website. 

@app.route('/')
def index():
	template = "index.html"
	return render_template(template)

# We need a place to store our template


#If this script is run from the command line
if __name__ == "__main__":
	# Fire up the Flask test server
	app.run(debug=True, use_reloader=True)
