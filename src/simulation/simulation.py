import requests
import random

class Fan:
    def __init__(self, **kwargs):
        self.fan_id = kwargs.get('id', -1)                                  # id
        self.status = kwargs.get('status')                                  # either S, I, or R
        self.days_since_infected = kwargs.get('days_since_infected', None)  # if not infected, None
        self.asymptomatic = kwargs.get('asymptomatic')                      # either true or false

class Sport:
    def __init__(self, **kwargs):
        self.sport_id = kwargs.get('id', -1)                            # id
        self.name = kwargs.get('name')                                  # name of sport
        self.num_events = kwargs.get('num_events')                      # num of events in season
        self.event_time_interval = kwargs.get('event_time_interval')    # days b/w events
        self.event_duration = kwargs.get('event_duration')              # length of event (in mins)
        self.env = kwargs.get('env')                                    # inside, outside, or both
    
    def print_name(self):
        print(self.name)

def initialize_fans(state_name):
    print(state_name)

def main():
    response = requests.get('https://api.covidtracking.com/v1/states/current.json')
    state_info_list = response.json()

    ca_info = None
    for state_info in state_info_list:
        if state_info['state'] == 'CA':
            ca_info = state_info

    # sport_list = []

    # baseball = Sport(id=0, name='baseball', num_events=162, event_time_interval=1.15, event_duration=185, env='O')
    # basketball = Sport(id=1, name='basketball', num_events=82, event_time_interval=2.15, event_duration=150, env='I')
    # football = Sport(id=2, name='football', num_events=16, event_time_interval=7.19, event_duration=192, env='B')
    # hockey = Sport(id=3, name='hockey', num_events=82, event_time_interval=2.26, event_duration=140, env='I')
    # racing = Sport(id=4, name='racing', num_events=36, event_time_interval=7.78, event_duration=180, env='O')
    # soccer = Sport(id=5, name='soccer', num_events=34, event_time_interval=6.41, event_duration=120, env='O')

    # sport_list.append(baseball)
    # sport_list.append(basketball)
    # sport_list.append(football)
    # sport_list.append(hockey)
    # sport_list.append(racing)
    # sport_list.append(soccer)

    # for x in sport_list:
    #     x.print_name()

    initialize_fans('california')

def random_sample():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_list = random.sample(test_list, 3)

    print(random_list)

if __name__ == "__main__":
    main()