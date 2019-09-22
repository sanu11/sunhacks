from twilio.twiml.voice_response import VoiceResponse, Gather,Say
from twilio import twiml
from flask import Flask, request
import os
import time
# from googlesearch import search
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
# chrome_options = Options()
# chrome_options.add_argument("--window-size=1024x768")
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="./chromedriver")


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
	"""Respond to incoming phone calls with a brief message."""
	# Start our TwiML response
	# resp = VoiceResponse()

	# # Read a message aloud to the caller
	# resp.say("Thank you for calling Sanika ! Have a great day.", voice='alice')

	# return str(resp)
	resp = VoiceResponse()

	# Start our <Gather> verb
	gather = Gather(num_digits=1)
	gather.say('For sales, press 1. For support, press 2.')
	resp.append(gather)
	print(gather)

	# If the user doesn't select an option, redirect them into a loop
	resp.redirect('/answer')

	return str(resp)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('For sales, press 1. For support, press 2.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect("/voice")

    return str(resp)


@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()
    # gather = Gather(timeout=30,)
    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('You selected sales. Good for you!')
            return str(resp)
        elif choice == '2':
            resp.say('You need support. We will help!')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")
    print(request.values)
    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/voice')

    return str(resp)

@app.route('/result', methods=['GET', 'POST'])
def result():
    # print(request['msg'])
    for key in request.values:
        print(key,request.values[key])
    

    response=request.values['SpeechResult']
    # response="What is the temperature in Tempe right now?"
    f = open("test.txt", "w+")
    f.write(str(response))
    time.sleep(30)
    # temp = "python3 -m textinput --device-id 'WinGAsstSanika' --device-model-id 'WinGAsstSanika' < test.txt"
    # os.system("google-oauthlib-tool --client-secrets ~/Desktop/Sanika/sunhacks/client_secret_972488926874-lce0kgbk1hrnv4bfgk4j31fms2ktvlrk.apps.googleusercontent.com.json  --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless")
    # ans=os.system(temp)
    # os.popen(temp).read() > 'test.txt'
   
    return response



@app.route('/speech', methods=['GET', 'POST'])
def speech():
    resp = VoiceResponse()
    gather = Gather(input="dtmf speech",finishOnKey="#",timeout="50",action="/result")
    gather.say("Thanks for the input, Sanika")
    resp.append(gather)
    f = open("output.txt")
    response = f.readlines()
    response = str(response).split('@')[1]
    response = response.split('>')[1].replace("\n","")
    # print(response)
    # print(resp)
    # print(gather)
    print(response)
    gather.say(str(response))
    
    return str(resp)


# @app.route('/query', methods=['GET', 'POST'])
# def query():
#     # Search for query
#     query="where is tokyo located in japan"
#     query = query.replace(' ', '+')

#     driver.get('http://www.google.com/search?q=' + query)

#     # Get text from Google answer box

#     answer = driver.execute_script(
#             "return document.elementFromPoint(arguments[0], arguments[1]);",
#             350, 230).text
#     print(answer)
#     return answer


if __name__ == "__main__":
	app.run(debug=True)


