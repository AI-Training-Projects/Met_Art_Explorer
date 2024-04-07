""""
https://collectionapi.metmuseum.org/public/collection/v1"
"""

import streamlit as st
import requests
import random

MET_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
OBJECTS = F'{MET_BASE_URL}/objects'
DEPARTMENTS = F'{MET_BASE_URL}/departments'

random.seed()

class Explorer:
    def __init__(self):
        self.departments = requests.get(DEPARTMENTS).json()
        self.department_id = None
        self.objects = []
        self.image = ""
    
    def show_rooms(self):
        for department in self.departments["departments"]:
            st.button(
                department["displayName"], 
                on_click=self.go_to_room, 
                kwargs={
                    "name": department["displayName"],
                    "department_id": department["departmentId"]
                    })
    
    def go_to_room(self, department_id, name):
        self.department_id = department_id
        self.department_name = name
        self.objects = requests.get(F'{OBJECTS}?departmentIds={department_id}').json()["objectIDs"]
        self.show_room()
    
    def show_room(self):
        self.get_random_obj()
        st.text(self.department_name)
        self.image = self.object["primaryImageSmall"]
        st.button(
            "Jump",
            on_click=self.show_room
        )
        self.show_image()
        st.markdown(F'<{self.object["objectURL"]}>')
        region = self.object["country"] or self.object["culture"] or self.object["artistNationality"]
        st.text(
            F'''
                Title: {self.object["title"]}
                Date: {self.object["objectDate"]}
                Location: {region}
                What is it? {self.object["classification"]}
            '''
        )
        

    def get_random_obj(self):
        object_index = random.randint(0, len(self.objects) - 1)
        self.objects[object_index]
        self.object = requests.get(F"{OBJECTS}/{self.objects[object_index]}").json()
    
    def show_image(self):
        if self.image != "":
            st.image(self.image)
        else:
            st.text("Ooops ... we don't have an image. Here is a cat instead!")
            cat = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]
            st.image(cat)
    
st.title("Explore The Met")
met_exporer_obj = Explorer()
met_exporer_obj.show_rooms()
