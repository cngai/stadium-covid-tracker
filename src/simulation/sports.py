class Sport:
    def __init__(self, **kwargs):
        self.sport_id = kwargs.get('id', -1)                            # id
        self.name = kwargs.get('name')                                  # name of sport
        self.num_events = kwargs.get('num_events')                      # num of events in season
        self.event_time_interval = kwargs.get('event_time_interval')    # days b/w events
        self.event_duration = kwargs.get('event_duration')              # length of event (in mins)
        self.env = kwargs.get('env')                                    # inside, outside, or both
        self.percentage_fans = kwargs.get('percentage_fans')            # percentage of sports fans (0-1)

sports_dict = {
    'baseball': Sport(id=0, name='baseball', num_events=162, event_time_interval=1.15, event_duration=185, env='O', percentage_fans=0.51),
    'basketball': Sport(id=1, name='basketball', num_events=82, event_time_interval=2.15, event_duration=150, env='I', percentage_fans=0.4),
    'football': Sport(id=2, name='football', num_events=16, event_time_interval=7.19, event_duration=192, env='B', percentage_fans=0.57),
    'hockey': Sport(id=3, name='hockey', num_events=82, event_time_interval=2.26, event_duration=140, env='I', percentage_fans=0.28),
    'racing': Sport(id=4, name='racing', num_events=36, event_time_interval=7.78, event_duration=180, env='O', percentage_fans=0.32),
    'soccer': Sport(id=5, name='soccer', num_events=34, event_time_interval=6.41, event_duration=120, env='O', percentage_fans=0.28)
}