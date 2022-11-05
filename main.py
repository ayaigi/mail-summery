import os
import yaml
from iterate import iterate
import datetime
import time

def main():
    # Store where we currently are in the filesystem.
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # Attempt to read in the configuration.
    with open(os.path.join(__location__, "config.yml"), 'r') as stream:
        try:
            config = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)
        
    sendtime = sorted(list(map(reTime, config['send_time'])))
    
    while(True):
        iterate(config, True)
        for time in sendtime:
            dt = next_time(time)
            print("wait until {}".format(dt))
            wait_until(dt)
            iterate(config)
        time.sleep(300)
                
def wait_until(end_datetime):
    while True:
        diff = (end_datetime - datetime.datetime.now()).total_seconds()
        if diff < 0: return       # In case end_datetime was in past to begin with
        time.sleep(diff/2)
        if diff <= 60: return
    
def reTime(t: str):
    return datetime.datetime.strptime(t, "%H:%M").time()

def next_time(t):
    now = datetime.datetime.now()
    dif = now - datetime.datetime.combine(now.date(), t)
    if dif.total_seconds() < 0:
        dt = datetime.datetime.combine(now.date(), t)
    else:
        dt = datetime.datetime.combine((now.date() + datetime.timedelta(days=1)), t)
    return dt
        
def timesecs(t):
    datetime.datetime.now().time()



main()