import random
import sys
from state_info import get_state_attr
from sports import sports_dict

class Fan:
    def __init__(self, **kwargs):
        self.fan_id = kwargs.get('id', -1)                                      # id
        self.status = kwargs.get('status')                                      # either S, I, or R
        self.days_since_infected = kwargs.get('days_since_infected', None)      # if not infected, None
        self.asymptomatic = kwargs.get('asymptomatic')                          # either true or false
        self.days_since_recovered = kwargs.get('days_since_recovered', None)    # if not recovered, None

def random_sample():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_list = random.sample(test_list, 3)

    print(random_list)

# INITIALIZATION PHASE

def get_sport_obj(sport_name):
    print(sports_dict[sport_name.lower()].percentage_fans)

def get_state_obj(state_name):
    state_obj = get_state_attr(state_name)
    print('Name: ' + state_obj.name)
    print('Abbreviation: ' + state_obj.abbrev)
    print('Population: ' + str(state_obj.population))
    print('Positives: ' + str(state_obj.positives))

    return state_obj

# get number of fans based on state and sport
def get_num_fans(state_name, sport_name):
    percentage_fans = sports_dict[sport_name.lower()].percentage_fans
    state_pop = get_state_attr(state_name).population
    num_fans = round(percentage_fans * state_pop)

    print(num_fans)
    return num_fans

if __name__ == "__main__":
    # get_state_obj(sys.argv[1])
    # get_sport_obj(sys.argv[1])
    get_num_fans(sys.argv[1], sys.argv[2])
