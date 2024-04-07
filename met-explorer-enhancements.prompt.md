Created By: Rich Lysakowski
Created By: 2024.03.25
Updated On: 2024.04.06

Update History: 
    met_art.py is the original version created by ???
    met_art_explorer_v1.py is the first set of enhancements
    met_art_ChatGPT_v1.py was enhanced using ChatGPT with the AI-Powered Dev Team on 4/6/2024
        Some bugs in this version were fixed using Phind on 4/6/2024

    TODO: met_art_ChatGPT_v1.py needs to be renamed to eliminate ChatGPT in the name.  Reintroduce "chat" or some "smart" name in a later version when one or more AI agents are incorporated.

# NTAI TRAINEES: feel free to pick any "TBD Enhancement" below to implement.  
## Create a feature branch with the name of your feature, work on that feature. Commit all your changes to your local git repository.
## When your new feature is ready to be merged, create and send a Pull Request to the repo admin for https://github.com/AI-Training-Projects/Met_Art_Explorer .  
## Your change, addition or enhancement will be review and merged appropriately.

# HIGHEST PRIORITY:  Usability

Enhance the functionality of the "Met Art" Streamlit application @met_art.py to give it a better user experience and more functionality.

For context, the NY Museum of Metropolitan Art ("The Met") provides the REST API that this application for fetching images of art located at the MET.  The REST API base endpoint is located at https://collectionapi.metmuseum.org/public/collection/v1.  The application current fetches and dislays art images organized by department, and provides a list of all objects by ID. 

TODO: add the original author's github repository link and attribution.  

## First Set of Enhancements:   

## DONE: Move the collection navigator to the left sidebar, and when the user selects an image button in the sidebar, display the image in the right side page.  

Second, at the top of the sidebar add buttons with the following functionality :

??? 1) "Random_Views" button random cycles through all available images in the collection, one button click at a time.  

2) "Fetch_All_Art" button fetches and stores ALL images in a local folder named "Fetched_Art_{date} with a date-stamp when the all objects were fetched.  Before fetching all images, first get and save the list of all object IDs using the API.  Limit the number of requests to 30 per second to avoid being blocked.  

2) DEVELOPER ENHANCEMENT: Add another page link at the bottom of the navigator to fetch the API documentation in a right-side page so that developers can explore ways to implement enhancements.  When the app is "finished" this page can be hidden from view.  


# TODO: Find out whether "piece" or "holding" is the correct term to use for an art piece in the MET collection.  Use the correct term in the application.
# TODO: Move the Title "Explore The Met" to the top of the right-side page.
# TODO: Add a horizontal divider after the "Explore The Met" title.
# TODO: Add a horizontal divider after the "Department Name".
# TODO: In the left sidebar, fix the display of the total number of art pieces in each department.  If the total number of art pieces is not available, display "N/A".
# TODO: Add a formatted profile for each Department, with the total number of art pieces in the department.
# TODO: Add a description of the art piece in the main page.  Move the Art Piece description to the right side of the page, underneath the Art Piece image.
# TODO: Add a button at the top of the right side page to fetch a new art piece from the same department.  Add this underneath the Department Name, and above the Art Piece description. 
# TODO: Add a button to fetch a new art piece from a different department. ???

# TODO: PERFORMANCE ENHANCEMENTS:  OUTLINE THE STEPS BELOW:
## Pre-fetch art_piece_ids for each department and store them in a local cache as SQLite database file.  Do this when the application starts.  DO NOT clear the cache when the user exits the application.  

## When a user navigates to a department, fetch and display the first art piece they requested using the MET API and store the image in a folder for that department.  Use the art_piece_ids cache to fetch and display art pieces for each department, rather than always fetching them every time the application runs.  
# While the user is viewing the first art piece from that department, check if ALL other art pieces from that department are already cached.  If all images are already cached, use the cached art images folder.  If they are not cached, use the MET API to fetch and cache the remaining art pieces for that department.  Put in a small random delays of at least 10 milliseconds between fetching each art piece to avoid overloading the MET API.

### Following Politeness Rules" conventions for parallel processing.
    [text](https://adrien.barbaresi.eu/blog/how-to-download-parallel-politeness-rules-python.html)

    [text](https://trafilatura.readthedocs.io/en/latest/downloads.html)

    [text](https://github.com/duyet/awesome-web-scraper)
    
## From then on, use the cache to display art pieces for each department.  DO NOT clear the cache when the user exits the application; give the user an option to clear the cache when they exit the application.  

## While a user is viewing art pieces from first department, make a background request to fetch art_pieces for the other departments and store them in the SQLite database file.  Use the cache to display art pieces for each department.   

## When the user exits the application, give them an option to clear the cache.  If they choose to clear the cache, delete the SQLite database file and the art images folder.  If they choose not to clear the cache, keep the SQLite database file and the art images folder for the next time the application runs.


4) Add a Catalog of Full Collections 

    ## FULL MET COLLECTIONS DATASET: 

    There is a github repository with information about 

    https://github.com/metmuseum/openaccess

    The metObjects.csv file (320MG) is a large catalog index of art images and other artifacts that are in the Met Holdings.  

    The header is as follows:

        Object Number,Is Highlight,Is Timeline Work,Is Public Domain,Object ID,Gallery Number,Department,AccessionYear,Object Name,Title,Culture,Period,Dynasty,Reign,Portfolio,Constituent ID,Artist Role,Artist Prefix,Artist Display Name,Artist Display Bio,Artist Suffix,Artist Alpha Sort,Artist Nationality,Artist Begin Date,Artist End Date,Artist Gender,Artist ULAN URL,Artist Wikidata URL,Object Date,Object Begin Date,Object End Date,Medium,Dimensions,Credit Line,Geography Type,City,State,County,Country,Region,Subregion,Locale,Locus,Excavation,River,Classification,Rights and Reproduction,Link Resource,Object Wikidata URL,Metadata Date,Repository,Tags,Tags AAT URL,Tags Wikidata URL

    Build a database schema and then import this dataset.  See Met website and githut to see if there any references to a SQL schema that is already available, i.e., the one they use internally, rather than a flat file CSV export. 

Build Some Additional Analytics Applications: 

    https://medium.com/@elijah.jarocki/the-metropolitan-museum-of-art-collection-api-data-analysis-modeling-and-forecasting-29d13e18d06e

##############################################################################

# Second Enhancements, continued

1) "AutoPlay" button that ccles through all images. 
2) "Timeline" Page, using the Knight Lab Streamlit Timeline component.  provide selectable themes and play sequences.  


ADD A DEVELOPERS DOCUMENTATION PAGE: 
    a) v1.0 Add a static "REST API Docs" page for Developers.  
       v1.0 Fetch the entire Met API Documentation page and render it as HTML page "as is". 
       The API documentation is located here:  https://metmuseum.github.io/

    b) v2.0+ Create a dynamic "Developers Gallery" Streamlit Form with interactive sections with database field "selectors" and "filters" that let the user select fields from dynamically-loaded pop-up / dropdown menus, and then images will then be fetched and loaded dynamically. 

# Third Enhancements: 
## Let users select and save an image for their computer desktop "wallpaper"
    See: https://github.com/rfauver/met_wallpapers

#######################################

https://streamlit.io/ | Streamlit • A faster way to build and share data apps

https://docs.streamlit.io/library/api-reference/layout/st.expander | st.expander - Streamlit Docs

https://github.com/streamlit/streamlit/wiki/Running-e2e-tests-and-updating-snapshots#playwright-e2e-tests | Running e2e tests and updating snapshots · streamlit/streamlit Wiki

https://metmuseum.github.io/ | Latest Updates | The Metropolitan Museum of Art Collection API

https://medium.com/@elijah.jarocki/

the-metropolitan-museum-of-art-collection-api-data-analysis-modeling-and-forecasting-29d13e18d06e | The Metropolitan Museum of Art Collection API — Data Analysis, Modeling, and Forecasting | by Elijah Jarocki | Medium

https://github.com/ejarocki/The-Met-API-Data-Analysis/blob/master/The-Met-API-Data-Analysis.pdf | The-Met-API-Data-Analysis/The-Met-API-Data-Analysis.pdf at master · ejarocki/The-Met-API-Data-Analysis

# Fake Art News Generator: 
    https://github.com/aarongermaine/met_art_generator

    User Story

    Because the novel coronavirus had a tremendous impact on everything we wanted to create a similar experience to browsing a museum.

    Acceptance Criteria:

        Ability to search for keywords
        Ability to filter by categories
        Display picture of the item in museum
        Display information that could be * found on information card
        Create an opportunity for art appreciation

    Description
    The Met Art Generator provides randomly generated art based on the user's search parameters. Additionally, the site displays the artist's name, title of work, time period, medium used, and location inside the Met. On the site, the user will have the option to follow the Come Visit Us! link to learn the history of the Met musuem and get the location from its interactive map.

######################################################################################################

##################
Project Europeana: 

Implement a similar Art Explorer for the art images available from the Project Europeana REST API.

