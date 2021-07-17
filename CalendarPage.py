from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

from NewEventPage import *

class CalendarPage(Screen):

    def __init__(self,navbar,**kwargs):
        super().__init__(**kwargs)
        self.__setattr__("orientation","vertical")
        self.navbar = navbar


    def create_page(self):

        box_layout_page = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(cols=7)
        week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for day in week_days:
            grid_layout.add_widget(Label(text=f"{day}",size_hint_y=None))

        for day in week_days:
            grid_layout_days = GridLayout(cols=1)
            self.ids[day] = grid_layout_days
            grid_layout.add_widget(self.ids[day])

        box_layout_page.add_widget(self.navbar)
        box_layout_page.add_widget(grid_layout)

        self.add_widget(box_layout_page)
        #self.update()
        return self

    def update(self,obj):
        try:
            with open('events.json') as json_file:
                event_dict = json.load(json_file)

            color_dict = {'Strength':(138,57,57),
                          'Endurance':(92,138,57),
                          'Intelligence':(57,84,138),
                          'Spirit':(219,216,116)
                          }

            for i in event_dict:
                current_obj = event_dict.get(i)
                if i not in self.ids:
                    for j in current_obj['days']:
                        button = Button(text=f"{current_obj['name']} \n"
                                                           f"{current_obj['type']} \n"
                                                           f"{current_obj['time_start'][0]}:00 -"
                                                           f" {current_obj['time_stop'][0]}:00",
                                                      size_hint=[1,None],
                                                      color=color_dict.get(current_obj['type']))
                        self.ids[j].add_widget(button)
                    self.ids[f'{i}'] = current_obj


        except:
            print('A bug appeared when trying to load events from json file, herhaps it is currently empty or missing')

