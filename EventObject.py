import json

class EventObject:
    def __init__(self,id,name,type,days,time_start,time_stop):
        self.name = name
        self.type = type
        self.days = days
        self.time_start = time_start
        self.time_stop = time_stop
        self.id = id

    def write_to_json(self):
        event_dict = self.__read_json_entries()
        event_dict[self.id] = {}
        event_dict[self.id]['name'] = self.name
        event_dict[self.id]['type'] = self.type
        event_dict[self.id]['days'] = self.days
        event_dict[self.id]['time_start'] = self.time_start
        event_dict[self.id]['time_stop'] = self.time_stop
        with open('events.json','w') as outfile:
            json.dump(event_dict,outfile)

    def __read_json_entries(self):
        try:
            with open('events.json') as json_file:
                dict = json.load(json_file)
            return dict
        except:
            return {}

