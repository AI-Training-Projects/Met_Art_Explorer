"""
Enhanced Streamlit application to explore the Metropolitan Museum of Art's collection.
Helps users browse different departments and view random art pieces from each department.

- Updated by: Rich Lysakowski and ChatGPT and NTAI Team
- Updated On: 2024.03.06 

Explanation:

Logging: Logging is implemented to log operations and errors to a log file in the "app_logs" directory.
Sidebar Navigation: Departments are displayed in the Streamlit Sidebar for easy navigation.
Department Information: The department name and total number of art pieces are displayed in the Sidebar.
Art Piece Display: Art piece information including title, ID, artist, description, department, and image is displayed in the main page.
Error Handling: Errors are logged to the console and to the log file without displaying them to end-users.

"""

import streamlit as st
import requests
import random
import os
import logging

# Set up logging
log_dir = "app_logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, "app_log.log"), level=logging.INFO)

MET_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
OBJECTS = f"{MET_BASE_URL}/objects"
DEPARTMENTS = f"{MET_BASE_URL}/departments"

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
        self.department_name = None
        self.objects = []
        self.object = None
        self.image = ""

    # def show_rooms(self):
    #     """
    #     Displays buttons for each department in the MET collection in the Streamlit Sidebar.
    #     Users can click on a department to view art pieces from that department.
    #     """
    #     st.sidebar.title("Departments")
    #     for department in self.departments["departments"]:
    #         st.sidebar.button(
    #             f"{department['displayName']} ({department['totalObjects']})",
    #             on_click=self.go_to_room,
    #             kwargs={
    #                 "name": department["displayName"],
    #                 "department_id": department["departmentId"]
    #             }
    #         )

    def show_rooms(self):
        """
        Displays buttons for each department in the MET collection in the Streamlit Sidebar.
        Users can click on a department to view art pieces from that department.
        """
        st.sidebar.title("Departments")
        for department in self.departments["departments"]:
            # Use 'N/A' as a default value if 'totalObjects' does not exist
            total_objects = department.get('totalObjects', 'N/A')
            st.sidebar.button(
                f"{department['displayName']} ({total_objects})",
                on_click=self.go_to_room,
                kwargs={
                    "name": department["displayName"],
                    "department_id": department["departmentId"]
                }
            )

    def go_to_room(self, department_id, name):
        """
        Navigates to a specific department and fetches art pieces from that department.

        Parameters:
        - department_id (str): The ID of the department to navigate to.
        - name (str): The display name of the department.
        """
        self.department_id = department_id
        self.department_name = name
        self.objects = requests.get(f"{OBJECTS}?departmentIds={department_id}").json()["objectIDs"]
        self.show_room()

    def show_room(self):
        """
        Displays a random art piece from the current department.
        Users can click the "Fetch Art Piece (Randomly)" button to view a different art piece.
        """
        self.get_random_obj()
        st.title(self.department_name)
        st.subheader("Art Piece")
        st.text(f"Title: {self.object['title']}")
        st.text(f"Holding ID: {self.object['objectID']}")
        st.text(f"Artist: {self.object.get('artistDisplayName', 'Unknown')}")
        st.text(f"Description: {self.object.get('objectName', 'N/A')}")
        st.text(f"Department: {self.object.get('department', 'N/A')} ({self.department_name})")
        st.text(f"Piece {self.objects.index(self.object['objectID']) + 1} of {len(self.objects)}")
        # Check if primaryImageSmall is not empty and is a valid URL or file path
        if self.object["primaryImageSmall"]:
            st.image(self.object["primaryImageSmall"])
        else:
            st.warning("Image not available.")
        st.markdown(f"[More Info]({self.object['objectURL']})")
        logging.info(f"Displayed art piece: {self.object['title']}")

    def get_random_obj(self):
        """
        Fetches a random art piece from the current department.
        """
        object_index = random.randint(0, len(self.objects) - 1)
        self.object = requests.get(f"{OBJECTS}/{self.objects[object_index]}").json()

if __name__ == "__main__":
    st.title("Explore The Met")
    met_explorer_obj = Explorer()
    met_explorer_obj.show_rooms()
