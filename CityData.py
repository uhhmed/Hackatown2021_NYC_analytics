from datetime import datetime

class CityData:
    def __init__(self, apiData):
        self.data = apiData
 
    # Return full JSON api data from...
    # data.cityofnewyork.us/Housing-Development/Active-Projects-Public-Buildings/
    def all_data(self):
        return self.data

    # sum total cost of all projects currently active/ongoing
    def sum_total_of_projects(self):
        totalSum = 0

        for cost in self.data:
            # remove unnecessary strings in order to convert to numbers to int.
            cleaned = cost['dollar_amount'].strip('$').replace('to', '')
            for indvPrice in cleaned:

                # assure current sting is a digit to convert and tally.
                if indvPrice.isdigit():
                    print(indvPrice)
                    totalSum += int(indvPrice)
        return totalSum

    # Return counts of each phase projects are in
    def phase_of_projects_counts(self):
        counts = {}
        for record in self.data:
            phase = record['phase']
            # check if phase type already exists, if so, increment
            if phase in counts.keys():
                counts[phase] += 1
            
            # set up new key with inital value of 1
            else:
                counts[phase] = 1

        return counts

    # Return counts of scheduled project completion dates
    def dateCompletion(self):
        counts = {}
        for record in self.data:
            date = record['projected_construction_completion']
            # reformat date string to shorten string on chart xAxis
            reformated = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
            reformated = datetime.strftime(reformated, "%b %Y")
            
            if reformated in counts.keys():
                counts[reformated] += 1
            else:
                counts[reformated] = 1

        # sort dict by date descending
        ordered_data = dict(sorted(counts.items()))
        return ordered_data

    
    