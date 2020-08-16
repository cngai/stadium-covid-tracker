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

state_attr_dict = {
    'alaska': State(name='Alaska', abbrev='AK', population=737438),
    'alabama': State(name='Alabama', abbrev='AL', population=4887871),
    'arkansas': State(name='Arkansas', abbrev='AR', population=3013825),
    'arizona': State(name='Arizona', abbrev='AZ', population=7171646),
    'california': State(name='California', abbrev='CA', population=39557045),
    'colorado': State(name='Colorado', abbrev='CO', population=5695564),
    'connecticut': State(name='Connecticut', abbrev='CT', population=3572665),
    'delaware': State(name='Delaware', abbrev='DE', population=967171),
    'florida': State(name='Florida', abbrev='FL', population=21299325),
    'georgia': State(name='Georgia', abbrev='GA', population=10519475),
    'hawaii': State(name='Hawaii', abbrev='HI', population=1420491),
    'iowa': State(name='Iowa', abbrev='IA', population=3156145),
    'idaho': State(name='Idaho', abbrev='ID', population=1754208),
    'illinois': State(name='Illinois', abbrev='IL', population=12741080),
    'indiana': State(name='Indiana', abbrev='IN', population=6691878),
    'kansas': State(name='Kansas', abbrev='KS', population=2911510),
    'kentucky': State(name='Kentucky', abbrev='KY', population=4468402),
    'louisiana': State(name='Louisiana', abbrev='LA', population=4659978),
    'massachusetts': State(name='Massachusetts', abbrev='MA', population=6902149),
    'maryland': State(name='Maryland', abbrev='MD', population=6042718),
    'maine': State(name='Maine', abbrev='ME', population=1338404),
    'michigan': State(name='Michigan', abbrev='MI', population=9995915),
    'minnesota': State(name='Minnesota', abbrev='MN', population=5611179),
    'missouri': State(name='Missouri', abbrev='MO', population=6126452),
    'mississippi': State(name='Mississippi', abbrev='MS', population=2986530),
    'montana': State(name='Montana', abbrev='MT', population=1062305),
    'north carolina': State(name='North Carolina', abbrev='NC', population=10383620),
    'north dakota': State(name='North Dakota', abbrev='ND', population=760077),
    'nebraska': State(name='Nebraska', abbrev='NE',  population=1929268),
    'new hampshire': State(name='New Hampshire', abbrev='NH', population=1356458),
    'new jersey': State(name='New Jersey', abbrev='NJ', population=8908520),
    'new mexico': State(name='New Mexico', abbrev='NM', population=2095428),
    'nevada': State(name='Nevada', abbrev='NV', population=3034392),
    'new york': State(name='New York', abbrev='NY', population=19542209),
    'ohio': State(name='Ohio', abbrev='OH', population=11689442),
    'oklahoma': State(name='Oklahoma', abbrev='OK', population=3943079),
    'oregon': State(name='Oregon', abbrev='OR', population=4190713),
    'pennsylvania': State(name='Pennsylvania', abbrev='PA', population=12807060),
    'rhode island': State(name='Rhode Island', abbrev='RI', population=1057315),
    'south carolina': State(name='South Carolina', abbrev='SC', population=5084127),
    'south dakota': State(name='South Dakota', abbrev='SD', population=882235),
    'tennessee': State(name='Tennessee', abbrev='TN', population=6770010),
    'texas': State(name='Texas', abbrev='TX', population=28701845),
    'utah': State(name='Utah', abbrev='UT', population=3161105),
    'virginia': State(name='Virginia', abbrev='VA', population=8517685),
    'vermont': State(name='Vermont', abbrev='VT', population=626299),
    'washington': State(name='Washington', abbrev='WA', population=7535591),
    'wisconsin': State(name='Wisconsin', abbrev='WI', population=5813568),
    'west virginia': State(name='West Virginia', abbrev='WV', population=1805832),
    'wyoming': State(name='Wyoming', abbrev='WY', population=577737),
}

# returns state object with updated num of positive cases
def get_state_attr(state_name):
    state_obj = None

    if state_name in state_attr_dict:
        state_obj = state_attr_dict[state_name]

    if state_obj:
        response = requests.get(f"https://api.covidtracking.com/v1/states/{state_obj.abbrev.lower()}/current.json")
        state_info_json = response.json()
        state_obj.update_positives(state_info_json['positive'])

    return state_obj

if __name__ == "__main__":
    get_state_attr(sys.argv[1])
