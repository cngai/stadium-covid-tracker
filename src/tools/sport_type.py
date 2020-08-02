from csv import reader, writer
import math

def main():
    # open file in read mode
    with open('../../public/data/Major_Sport_Venues_Usage.csv', 'r') as sport_data:
        csv_reader = reader(sport_data)
        header_line = next(csv_reader) # skip header line

        # league-specific info
        league_dict = {} # dictionary that stores league name to total stadium capacity and num of stadiums
        
        # major vs minor league info
        major_baseball = ['MLB']
        major_baseball_count = [0, 0]
        minor_baseball = ['MILB']
        minor_baseball_count = [0, 0]
        major_basketball = ['NBA']
        major_basketball_count = [0, 0]
        minor_basketball = ['WNBA', 'NCAA DIVISION 1 BASKETBALL']
        minor_basketball_count = [0, 0]
        major_football = ['NFL']
        major_football_count = [0, 0]
        minor_football = ['NCAA DIVISION 1-FBS FOOTBALL']
        minor_football_count = [0, 0]

        # sport type info
        baseball = ['MLB', 'MILB']
        baseball_count = [0, 0]
        basketball = ['NBA', 'WNBA', 'NCAA DIVISION 1 BASKETBALL']
        basketball_count = [0, 0]
        football = ['NFL', 'NCAA DIVISION 1-FBS FOOTBALL']
        football_count = [0, 0]
        # golf = ['PGA']
        # golf_count = [0, 0]
        hockey = ['NHL']
        hockey_count = [0, 0]
        horse_racing = ['HORSE RACE TRACK']
        horse_racing_count = [0, 0]
        racing = ['IRL', 'NASCAR']
        racing_count = [0, 0]
        soccer = ['MLS']
        soccer_count = [0, 0]

        if header_line != None:
            # iterate over each row in the csv using the csv_reader
            for row in csv_reader:
                league = row[2]
                stadium_cap = int(row[3])

                # skip any invalid entry (i.e. capacity is -999)
                if stadium_cap == -999:
                    continue

                # add league to lead dictionary if not in there already
                if league in league_dict:
                    temp_count = league_dict[league][0]
                    temp_cap = league_dict[league][1]
                    temp_count += 1
                    temp_cap += stadium_cap
                    league_dict[league] = [temp_count, temp_cap]
                else:
                    league_dict[league] = [1, stadium_cap]  # number of stadiums should start at 1

                # distinguish major vs. minor sports leagues
                if league in major_baseball:
                    major_baseball_count[0] = major_baseball_count[0] + 1
                    major_baseball_count[1] = major_baseball_count[1] + stadium_cap
                elif league in minor_baseball:
                    minor_baseball_count[0] = minor_baseball_count[0] + 1
                    minor_baseball_count[1] = minor_baseball_count[1] + stadium_cap
                elif league in major_basketball:
                    major_basketball_count[0] = major_basketball_count[0] + 1
                    major_basketball_count[1] = major_basketball_count[1] + stadium_cap
                elif league in minor_basketball:
                    minor_basketball_count[0] = minor_basketball_count[0] + 1
                    minor_basketball_count[1] = minor_basketball_count[1] + stadium_cap
                elif league in major_football:
                    major_football_count[0] = major_football_count[0] + 1
                    major_football_count[1] = major_football_count[1] + stadium_cap
                elif league in minor_football:
                    minor_football_count[0] = minor_football_count[0] + 1
                    minor_football_count[1] = minor_football_count[1] + stadium_cap

                # distinguish by sport type
                if league in baseball:
                    baseball_count[0] = baseball_count[0] + 1
                    baseball_count[1] = baseball_count[1] + stadium_cap
                elif league in basketball:
                    basketball_count[0] = basketball_count[0] + 1
                    basketball_count[1] = basketball_count[1] + stadium_cap
                elif league in football:
                    football_count[0] = football_count[0] + 1
                    football_count[1] = football_count[1] + stadium_cap
                # elif league in golf:
                #     golf_count[0] = golf_count[0] + 1
                #     golf_count[1] = golf_count[1] + stadium_cap
                elif league in hockey:
                    hockey_count[0] = hockey_count[0] + 1
                    hockey_count[1] = hockey_count[1] + stadium_cap
                elif league in horse_racing:
                    horse_racing_count[0] = horse_racing_count[0] + 1
                    horse_racing_count[1] = horse_racing_count[1] + stadium_cap
                elif league in racing:
                    racing_count[0] = racing_count[0] + 1
                    racing_count[1] = racing_count[1] + stadium_cap
                elif league in soccer:
                    soccer_count[0] = soccer_count[0] + 1
                    soccer_count[1] = soccer_count[1] + stadium_cap

        # calculate averages
        league_averages = {}
        for x in league_dict:
            league_avg_cap = league_dict[x][1] / league_dict[x][0]
            league_averages[x] = math.floor(league_avg_cap) # round down

        major_baseball_avg = math.floor(major_baseball_count[1] / major_baseball_count[0])
        minor_baseball_avg = math.floor(minor_baseball_count[1] / minor_baseball_count[0])
        major_basketball_avg = math.floor(major_basketball_count[1] / major_basketball_count[0])
        minor_basketball_avg = math.floor(minor_basketball_count[1] / minor_basketball_count[0])
        major_football_avg = math.floor(major_football_count[1] / major_football_count[0])
        minor_football_avg = math.floor(minor_football_count[1] / minor_football_count[0])

        baseball_avg = math.floor(baseball_count[1] / baseball_count[0])
        basketball_avg = math.floor(basketball_count[1] / basketball_count[0])
        football_avg = math.floor(football_count[1] / football_count[0])
        # golf_avg = math.floor(golf_count[1] / golf_count[0])
        hockey_avg = math.floor(hockey_count[1] / hockey_count[0])
        horse_racing_avg = math.floor(horse_racing_count[1] / horse_racing_count[0])
        racing_avg = math.floor(racing_count[1] / racing_count[0])
        soccer_avg = math.floor(soccer_count[1] / soccer_count[0])

        # write to csv files
        with open('../../public/data/stadium_cap_by_league.csv', 'w', newline='') as league_file:
            csv_writer = writer(league_file)

            csv_writer.writerow(['LEAGUE_NAME', 'AVG_CAP'])
            for league_name in league_averages:
                csv_writer.writerow([league_name, league_averages[league_name]])

        with open('../../public/data/stadium_cap_by_scale.csv', 'w', newline='') as scale_file:
            csv_writer = writer(scale_file)

            csv_writer.writerow(['SPORT_TYPE', 'SCALE', 'AVG_CAP'])
            csv_writer.writerow(['Baseball', 'Major', major_baseball_avg])
            csv_writer.writerow(['Baseball', 'Minor', minor_baseball_avg])
            csv_writer.writerow(['Basketball', 'Major', major_basketball_avg])
            csv_writer.writerow(['Basketball', 'Minor', minor_basketball_avg])
            csv_writer.writerow(['Football', 'Major', major_football_avg])
            csv_writer.writerow(['Football', 'Minor', minor_football_avg])

        with open('../../public/data/stadium_cap_by_sport.csv', 'w', newline='') as sport_file:
            csv_writer = writer(sport_file)

            csv_writer.writerow(['SPORT_TYPE', 'AVG_CAP'])
            csv_writer.writerow(['Baseball', baseball_avg])
            csv_writer.writerow(['Basketball', basketball_avg])
            csv_writer.writerow(['Football', football_avg])
            csv_writer.writerow(['Hockey', hockey_avg])
            csv_writer.writerow(['Horse Racing', horse_racing_avg])
            csv_writer.writerow(['Racing', racing_avg])
            csv_writer.writerow(['Soccer', soccer_avg])

if __name__ == "__main__":
    main()