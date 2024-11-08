import requests

key = 'QNGCZNYQQNFIC7V8'  # Follow the steps below to get your key
t = 22

while True:
    t += 1
    print("temperature", t)
    params = {'field1': t, 'key': key}
    response = requests.post("https://api.thingspeak.com/update", data=params)
    print(response)


# Things you should follow before running your code
# Step 1:
#   - Create or login your ThingSpeak account on "thingspeak.mathworks.com"
# Step 2:
#   - Create New Channel
# Step 3:
#   - Give any Name to Channel, and click "Save Channel"
# Step 4:
#   - Go on to "Sharing" tab, select "Share channel view with everyone" (2nd option)
# Step 5:
#   - Finally go to "API Keys" tab, Copy the "Write API Key", that's your key


# After executing the program, Go on to the "Public view" tab, you will see your temperature value being updated every moment