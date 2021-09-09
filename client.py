import socket
import requests

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 4444))

    data_x = requests.get('http://13.233.13.254:2222/xenergyData.json').json()
    data_y = str(data_x['records'][len(data_x['records']) - 1])

    data_y = data_y.replace('None', 'null')
    data_y = data_y.replace('\'', '\"')

    temp = data_y

    client.send(data_y.encode())

    with open("data.json", "a") as text_file:
        text_file.write(data_y + ',\n')

    while True:
        data_x = requests.get('http://13.233.13.254:2222/xenergyData.json').json()
        data_y = str(data_x['records'][len(data_x['records']) - 1])

        data_y = data_y.replace('None', 'null')
        data_y = data_y.replace('\'', '\"')

        print(data_y)

        if data_y != temp:
            temp = data_y

            client.send(data_y.encode())

            with open("data.json", "a") as text_file:
                text_file.write(data_y.replace('None', 'null') + ',\n')