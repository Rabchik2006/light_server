import time,json,os
import RPi.GPIO as GP

GP.setmode(GP.BCM)
pin=int(os.environ.get('LIGHT_PIN'))
GP.setup(pin,GP.OUT)

def get_time():
    time_now=time.localtime(time.time())
    h=time_now[3]
    m=time_now[4]
    return [h,m]

def loop():
    while True:
        with open('data.json', 'r') as f:
            data=json.load(f)
        if get_time()==[data['hour'],data['minute']]:
            cond='yes'
            GP.output(pin,data['condition'])
        else:
            cond='no'
        print({cond}, f'Требeуется {data["hour"]}:{data["minute"]} Текущее: {get_time()[0]}:{get_time()[1]}')
        time.sleep(60)
loop()
