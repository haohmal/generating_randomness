filtered_data = ""
valid_charcters = ["0", "1"]
print("Please give AI some data to learn...")
while len(filtered_data) < 100:
    print("Current data length is " + str(len(filtered_data)) + ", " + str(100 - len(filtered_data)) + " symbols left")
    print("Print a random string containing 0 or 1:")
    data = input()
    for i in data:
        if i in valid_charcters:
            filtered_data += i


print("Final data string:")
print(filtered_data)

triad_templates = ['000', '001', '010', '011', '100', '101', '110', '111']

triads = {k: {"zero": 0, "one": 0} for k in triad_templates}
#triads['000']['one'] += 1
for i in range(len(filtered_data) -3):
    #print(filtered_data[i:i+3])
    if filtered_data[i+3] == '0':
        triads[filtered_data[i:i+3]]['zero'] += 1
    else:
        triads[filtered_data[i:i + 3]]['one'] += 1

#for triad in triad_templates:
    #print(triad + ": " + str(triads[triad]['zero']) + "," + str(triads[triad]['one']))
    #print(triad + ": " + triad['zero'] + "," + triad['one'])

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")

balance = 1000

data = ""
while data != "enough":
    data = ""
    filtered_data = ""
    print("Print a random string containing 0 or 1:")
    data = input()

    if data != "enough":
        prediction = "110"
        for i in data:
            if i in valid_charcters:
                filtered_data += i

        for i in range(len(filtered_data) -3):
            if triads[filtered_data[i:i+3]]['zero'] > triads[filtered_data[i:i+3]]['one']:
                prediction += "0"
            else:
                prediction += "1"

        print("prediction:")
        print(prediction)

        #print(len(data))
        #print(len(prediction))

        correct = 0
        if len(filtered_data) > 3:
            for i in range(len(filtered_data) -3):
                if filtered_data[i + 3] == prediction[i + 3]:
                    correct += 1

            print("Computer guessed right " + str(correct) + " out of " + str(len(filtered_data) - 3) + " symbols (" + str(round(correct * 100 / (len(filtered_data) - 3), 2)) + " %)")
            balance -= correct
            balance += len(filtered_data) - 3 - correct
            print("Your balance is now $" + str(balance))

    else:
        print("Game over!")