import time,os

while True:

    os.system('cls')
    localtm = time.localtime()
    result = time.strftime("%I:%M:%S %p",localtm)
    print(result)
    time.sleep(1)