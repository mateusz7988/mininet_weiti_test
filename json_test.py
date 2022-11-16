import os, json, uuid, requests





if __name__ == '__main__':

    print('Give path to file without extension:')
    nazwa = input()
    file = f"{nazwa}.json"
    global ID
    global json_file

    def changeSwitch():
        print('Do you want to edit deviceID? y/n ')
        ans=input()
        if ans == 'y':
            print('Give new deviceID: ')
            try:
                switch_id = int(input())
                if switch_id == 10:
                    ID = f"of:00000000000000{switch_id}"
                elif switch_id < 10:
                    ID = f"of:000000000000000{switch_id}"
                else:
                    print('There is no device with that ID!')
            except:
                print('deviceID must be Integer!')
            with open(file, 'r') as f:
                data = json.load(f)
                data['deviceId'] = ID
                f.close()
                os.remove(file)
            tempfile = os.path.join(os.path.dirname(file), str(uuid.uuid4()))
            with open(tempfile, 'w') as f:
                json.dump(data, f, indent=4)
                f.close()
                tempfile = json_file
                os.rename(tempfile, file)
        elif ans == 'n':
            None
        else:
            print("Sorry I don't understand.")
            changeSwitch()


    def changeInPort():
        print('Do you want to edit IN_PORT? y/n ')
        ans=input()
        if ans == 'y':
            print('Give new IN_PORT')
            try:
                input_port = int(input())
            except:
                print('IN_PORT must be Integer!')
                changeInPort()
            else:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data['selector']['criteria'][0]['port'] = input_port
                    f.close()
                    os.remove(file)
                tempfile = os.path.join(os.path.dirname(file), str(uuid.uuid4()))
                with open(tempfile, 'w') as f:
                    json.dump(data, f, indent=4)
                    f.close()
                    tempfile = json_file
                    os.rename(tempfile, file)

        elif ans == 'n':
            None
        else:
            print("Sorry I don't understand.")
            changeInPort()

    def changeOutput():
        print('Do you want to edit OUTPUT? y/n ')
        ans=input()
        if ans == 'y':
            print('Give new OUTPUT')
            try:
                output_port = int(input())
            except:
                print('IN_PORT must be Integer!')
                changeOutput()
            else:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data['treatment']['instructions'][0]['port'] = output_port
                    f.close()
                    os.remove(file)
                tempfile = os.path.join(os.path.dirname(file), str(uuid.uuid4()))
                with open(tempfile, 'w') as f:
                    json.dump(data, f, indent=4)
                    f.close()
                    tempfile = json_file
                    os.rename(tempfile, file)
        elif ans == 'n':
            None
        else:
            print("Sorry I don't understand.")
            changeOutput()



    changeSwitch()
    changeInPort()
    changeOutput()
    print(ID)
    url = f"http://192.168.1.102:8181/onos/v1/flows/{ID}"
    requests.post(url, json=json_file, auth=('karaf', 'karaf'), headers={"Content-Type": "application/json", "Accept": "application/json"})
