import requests
import sys

class State:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')              # name of state
        self.abbrev = kwargs.get('abbrev')          # abbreviation of state
        self.population = kwargs.get('population')  # population of state
        self.positives = None                       # total current positives in state

    # update number of positive cases based on API call
    def update_positives(self, num_pos):
        self.positives = num_pos

state_attr_list = [
    State(name='Alaska', abbrev='AK', population=737438),
    State(name='Alabama', abbrev='AL', population=4887871),
    State(name='Arkansas', abbrev='AR', population=3013825),
    State(name='Arizona', abbrev='AZ', population=7171646),
    State(name='California', abbrev='CA', population=39557045),
    State(name='Colorado', abbrev='CO', population=5695564),
    State(name='Connecticut', abbrev='CT', population=3572665),
    State(name='Delaware', abbrev='DE', population=967171),
    State(name='Florida', abbrev='FL', population=21299325),
    State(name='Georgia', abbrev='GA', population=10519475),
    State(name='Hawaii', abbrev='HI', population=1420491),
    State(name='Iowa', abbrev='IA', population=3156145),
    State(name='Idaho', abbrev='ID', population=1754208),
    State(name='Illinois', abbrev='IL', population=12741080),
    State(name='Indiana', abbrev='IN', population=6691878),
    State(name='Kansas', abbrev='KS', population=2911510),
    State(name='Kentucky', abbrev='KY', population=4468402),
    State(name='Louisiana', abbrev='LA', population=4659978),
    State(name='Massachusetts', abbrev='MA', population=6902149),
    State(name='Maryland', abbrev='MD', population=6042718),
    State(name='Maine', abbrev='ME', population=1338404),
    State(name='Michigan', abbrev='MI', population=9995915),
    State(name='Minnesota', abbrev='MN', population=5611179),
    State(name='Missouri', abbrev='MO', population=6126452),
    State(name='Mississippi', abbrev='MS', population=2986530),
    State(name='Montana', abbrev='MT', population=1062305),
    State(name='North Carolina', abbrev='NC', population=10383620),
    State(name='North Dakota', abbrev='ND', population=760077),
    State(name='Nebraska', abbrev='NE',  population=1929268),
    State(name='New Hampshire', abbrev='NH', population=1356458),
    State(name='New Jersey', abbrev='NJ', population=8908520),
    State(name='New Mexico', abbrev='NM', population=2095428),
    State(name='Nevada', abbrev='NV', population=3034392),
    State(name='New York', abbrev='NY', population=19542209),
    State(name='Ohio', abbrev='OH', population=11689442),
    State(name='Oklahoma', abbrev='OK', population=3943079),
    State(name='Oregon', abbrev='OR', population=4190713),
    State(name='Pennsylvania', abbrev='PA', population=12807060),
    State(name='Rhode Island', abbrev='RI', population=1057315),
    State(name='South Carolina', abbrev='SC', population=5084127),
    State(name='South Dakota', abbrev='SD', population=882235),
    State(name='Tennessee', abbrev='TN', population=6770010),
    State(name='Texas', abbrev='TX', population=28701845),
    State(name='Utah', abbrev='UT', population=3161105),
    State(name='Virginia', abbrev='VA', population=8517685),
    State(name='Vermont', abbrev='VT', population=626299),
    State(name='Washington', abbrev='WA', population=7535591),
    State(name='Wisconsin', abbrev='WI', population=5813568),
    State(name='West Virginia', abbrev='WV', population=1805832),
    State(name='Wyoming', abbrev='WY', population=577737),
]

# returns state object with updated num of positive cases
def get_state_attr(state_name):
    state_obj = None

    for state_attr in state_attr_list:
        if state_name.lower() == state_attr.name.lower():
            state_obj = state_attr
            break

    if state_obj:
        response = requests.get(f"https://api.covidtracking.com/v1/states/{state_obj.abbrev.lower()}/current.json")
        state_info_json = response.json()
        state_obj.update_positives(state_info_json['positive'])

    return state_obj

if __name__ == "__main__":
    get_state_attr(sys.argv[1])
