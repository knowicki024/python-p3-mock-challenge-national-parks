import ipdb

class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name') and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Invalid name")
        
    def trips(self):
        return self._trips
    
    def visitors(self):
        return list (set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if len(self._visitors) == 0:
            return None
        
        return max(self._visitors, key = self._visitors.count)


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.visitor._trips.append(self)
        self.visitor._national_parks.append(self.national_park)
        self.national_park._trips.append(self)
        self.national_park._visitors.append(self.visitor)

        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor 
    
    @visitor.setter 
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor 
        else:
            raise Exception("Visitor must be of class Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter 
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("National park must be of class National Park")
        
    @property 
    def start_date(self):
        return self._start_date 
    
    @start_date.setter 
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception("Start date must be string longer than 6 length")
        
    @property 
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7: 
            self._end_date = end_date
        else:
            raise Exception("End date must be string longer than 6 len")


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_park = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("not valid")
        
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(set(self._national_parks))
    
    def total_visits_at_park(self, park):
        total_visits = 0

        for nat_park in self._national_parks:
            if park == nat_park:
                total_visits += 1

        return total_visits

ipdb.set_trace()