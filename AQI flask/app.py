from flask import Flask, render_template, url_for, request
from requests import get
from json import loads

app = Flask(__name__)


def getdata(zipcode):
    try:
        varAPI = get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY={apikey}'.format(
            zipcode=zipcode, apikey='B9B759FC-6C22-496B-BEE2-2025217AE65C')
        )
        varJSON = loads(varAPI.content)
        area = varJSON[0]['ReportingArea']
        state = varJSON[0]['StateCode']
        lat = str(varJSON[0]['Latitude'])
        long = str(varJSON[0]['Longitude'])
        aqiO3 = varJSON[0]['AQI']
        statusO3 = varJSON[0]['Category']['Name']
        aqiPM25 = varJSON[1]['AQI']
        statusPM25 = varJSON[0]['Category']['Name']

        if statusO3 == "Good":
            colorO3 = "#acfaac"
        elif statusO3 == "Moderate":
            colorO3 = "#f6faac"
        elif statusO3 == "Unhealthy for Sensitive Groups":
            colorO3 = "#facdac"
        elif statusO3 == "Unhealthy":
            colorO3 = "#faacac"
        elif statusO3 == "Very Unhealthy":
            colorO3 = "#e4acfa"
        else:
            colorO3 = "#e4acfa"

        if statusPM25 == "Good":
            colorSP25 = "#acfaac"
        elif statusPM25 == "Moderate":
            colorSP25 = "#f6faac"
        elif statusPM25 == "Unhealthy for Sensitive Groups":
            colorSP25 = "#facdac"
        elif statusPM25 == "Unhealthy":
            colorSP25 = "#faacac"
        elif statusPM25 == "Very Unhealthy":
            colorSP25 = "#e4acfa"
        else:
            colorSP25 = "#e4acfa"

        data = [area+', '+state,
                lat+', '+long,
                aqiO3,
                statusO3,
                colorO3,
                aqiPM25,
                statusPM25,
                colorSP25]
        return data

    except IndexError:
        data = ["Check your zip code!",
                "0.0000, 0.0000",
                "0.00",
                "No status",
                "Zip code wrong",
                "0.00",
                "No status",
                "Zip code wrong"]
        return data

    except:
        data = ["Failed to connect!",
                "0.0000, 0.0000",
                "0.00",
                "No status",
                "Zip code wrong",
                "0.00",
                "No status",
                "Zip code wrong"]
        return data


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        data = getdata(zipcode)
        return render_template('result.html', data=data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
