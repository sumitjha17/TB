import requests,json
from flask import *


app = Flask(__name__)
app.config["DEBUG"] = True


capitalCityDict={}
longitudeDict={}
latitudeDict={}
countryName=[]


@app.route('/', methods=['GET'])
def home():

	try:
		myResponse=requests.get('http://api.worldbank.org/v2/country/?format=json')
		jData=json.loads(myResponse.content)
		if (myResponse.status_code==200):

			for jData2 in jData[1]:
				countryName.append(jData2['name'])
				if jData2['capitalCity']=='':
					capitalCityDict[jData2['name']]="Data Not Available"
				else:
					capitalCityDict[jData2['name']] = jData2['capitalCity']
				if jData2['longitude'] == '':
					longitudeDict[jData2['name']] = "Data Not Available"
				else:
					longitudeDict[jData2['name']] =jData2['longitude']
				if jData2['latitude'] == '':
					latitudeDict[jData2['name']] = "Data Not Available"
				else:
					latitudeDict[jData2['name']] = jData2['latitude']
			#print (countryName)
			try:
				return render_template('index.html',countryName=countryName)
			except:
				return "Template Could Not be Rendered"

		elif (myResponse.status_code==404):
			return myResponse.status_code +"           API Page not found"


		elif (myResponse.status_code==400):
			return myResponse.status_code +"           BAD Request Server Cannot Process"


		elif (myResponse.status_code==500):
			return myResponse.status_code +"           Internal Server Error"

	except:
		return "There was some Error while calling API"

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		country = request.form['countries']
		capital=capitalCityDict[country]
		longitude=longitudeDict[country]
		latitude=latitudeDict[country]

		try:
			return render_template("result.html",country=country,countryName=countryName,capital = capital,longitude=longitude,latitude=latitude)
			#return country
		except:
			return "Template Could Not be Rendered"






if __name__ == '__main__':
   app.run(debug = True)
