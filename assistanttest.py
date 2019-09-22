import os
import textinput
import subprocess

response="What is the temperature in Tempe right now?"
f = open("test.txt", "w+")
f.write(response)
temp = ""
# os.system("google-oauthlib-tool --client-secrets ~/Desktop/Sanika/sunhacks/client_secret_972488926874-lce0kgbk1hrnv4bfgk4j31fms2ktvlrk.apps.googleusercontent.com.json  --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless")
ans=os.system(temp)
# op=os.system("ls")
# subprocess.popen("", shell=True).read()
cmd="python3 -m textinput --device-id 'WinGAsstSanika' --device-model-id 'WinGAsstSanika' -v < test.txt"
# cmd = 'python train_frcnn.py --input_weight_path model_frcnn.hdf5 -o simple -p take2.csv'
subprocess.call(cmd, shell=True)
# print(ans)
# os.popen(temp).read() > 'test.txt'