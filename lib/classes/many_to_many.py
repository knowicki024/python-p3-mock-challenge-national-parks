class NationalPark:
    all = []

    def __init__(self, name):
        self._name = name
        NationalPark.all.append(self)

    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name 

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max (set(visitors), key = visitors.count)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter 
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and (start_date.endswith("st") or start_date.endswith("nd") or start_date.endswith("rd") or start_date.endswith("th")):
            self._start_date = start_date

    @property 
    def end_date(self):
        return self._end_date 
    
    @end_date.setter 
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7 and (end_date.endswith("st") or end_date.endswith("nd") or end_date.endswith("rd") or end_date.endswith("th")):
            self._end_date = end_date
    
    @property 
    def visitor(self):
        return self._visitor
    
    @visitor.setter 
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property 
    def national_park(self):
        return self._national_park 
    
    @national_park.setter 
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park 


class Visitor:
    all = []

    def __init__(self, name):
        self._name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name 

    def trips(self):
        return [ trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        if not park.visitors():
            return 0 
        return len([trip for trip in self.trips() if trip.national_park == park])