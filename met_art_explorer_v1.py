"""
Streamlit application to explore the Metropolitan Museum of Art's collection.
Helps users browse different departments and view random art pieces from each department.

- Updated by: Rich Lysakowski
- Updated On: 2024.03.25 
"""

import streamlit as st
import requests
import random

MET_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
OBJECTS = F'{MET_BASE_URL}/objects'
DEPARTMENTS = F'{MET_BASE_URL}/departments'

random.seed()

class Explorer:
    """
    A class to explore the Metropolitan Museum of Art's collection.
    It fetches department information and allows users to view random art pieces from each department.
    """
    
    def __init__(self):
        """
        Initializes the Explorer class by fetching department information from the MET API.
        """
        self.departments = requests.get(DEPARTMENTS).json()
        self.department_id = None
        self.objects = []
        self.image = ""
    
    def show_rooms(self):
        """
        Displays buttons for each department in the MET collection.
        Users can click on a department to view art pieces from that department.
        """
        print(f"The list of departments from self.departments['departments'] is {self.departments["departments"]}")

        for department in self.departments["departments"]:
            # a button is created for each department in the list of departments
            print(f"department ['displayName'] is {department['displayName']}")
            print(f"department ['departmentId'] is {department['departmentId']}")
            st.button(
                department["displayName"], 
                on_click=self.go_to_room, 
                kwargs={
                    "name": department["displayName"],
                    "department_id": department["departmentId"]
                    })
    
    def go_to_room(self, department_id, name):
        """
        Navigates to a specific department and fetches art pieces from that department.
        
        Parameters:
        - department_id (str): The ID of the department to navigate to.
        - name (str): The display name of the department.
        """
        self.department_id = department_id
        self.department_name = name
        self.objects = requests.get(F'{OBJECTS}?departmentIds={department_id}').json()["objectIDs"]
        self.show_room()
        print(f"List of objects accessed by go_to_room(): {self.show_room()} ")
    
    def show_room(self):
        """
        Displays a random art piece from the current department.
        Users can click the "Jump" button to view a different art piece.
        """
        self.get_random_obj()
        st.text(self.department_name)
        self.image = self.object["primaryImageSmall"]
        st.button(
            "Show Me Some Art!",
            on_click=self.show_room
        )
        self.show_image()
        st.markdown(F'<{self.object["objectURL"]}>')
        region = self.object["country"] or self.object["culture"] or self.object["artistNationality"]
        st.text(
            F'''
                Title: {self.object["title"]}
                Holding ID: {self.object["title"]}
                Date: {self.object["objectDate"]}
                Location: {region}
                What is it? {self.object["classification"]}
            '''
        )
    
    def get_random_obj(self):
        """
        Fetches a random art piece from the current department.
        """
        object_index = random.randint(0, len(self.objects) - 1)
        self.objects[object_index]
        self.object = requests.get(F"{OBJECTS}/{self.objects[object_index]}").json()
    
    def show_image(self):
        """
        Displays the image of the current art piece.
        If no image is available, it displays a random cat image instead.
        """
        if self.image != "":
            st.image(self.image)
        else:
            st.text("Ooops ... we don't have an image. Here is a cat instead!")
            cat = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]
            st.image(cat)

st.title("Explore The Met")
met_exporer_obj = Explorer()
met_exporer_obj.show_rooms()

# MET_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
# OBJECTS = F'{MET_BASE_URL}/objects'
# DEPARTMENTS = F'{MET_BASE_URL}/departments'

#object1 = https://collectionapi.metmuseum.org/public/collection/v1/objects
#department1 = https://collectionapi.metmuseum.org/public/collection/v1/DEPARTMENTS
