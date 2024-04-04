Created By: Rich Lysakowski
Updated By: 2024.03.25
Updated On: 

Enhance the functionality of the "Met Art" Streamlit application @met_art.py to give it a better user experience and more functionality.

For context, the NY Museum of Metropolitan Art ("The Met") provides the REST API that this application for fetching images of art located at the MET.  The REST API base endpoint is located at https://collectionapi.metmuseum.org/public/collection/v1.  The application current fetches and dislays art images organized by department, and provides a list of all objects by ID. 

# First Set of Enhancements:   
    
First, we want to move navigation to a left-side navigator.  

Move the collection navigator to the left sidebar, and when the user selects an image button in the sidebar, display the image in the right side page.  

Second, at the top of the sidebar add buttons with the following functionality :

1) "Random_Views" button random cycles through all available images in the collection, one button click at a time.  

2) "Fetch_All_Art" button fetches and stores ALL images in a local folder named "Fetched_Art_{date} with a date-stamp when the all objects were fetched.  Before fetching all images, first get and save the list of all object IDs using the API.  Limit the number of requests to 30 per second to avoid being blocked.  

3) Add another page to fetch the explore the API documentation.  

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


#######################################

https://streamlit.io/ | Streamlit • A faster way to build and share data apps

https://docs.streamlit.io/library/api-reference/layout/st.expander | st.expander - Streamlit Docs

https://github.com/streamlit/streamlit/wiki/Running-e2e-tests-and-updating-snapshots#playwright-e2e-tests | Running e2e tests and updating snapshots · streamlit/streamlit Wiki

https://metmuseum.github.io/ | Latest Updates | The Metropolitan Museum of Art Collection API

https://medium.com/@elijah.jarocki/

the-metropolitan-museum-of-art-collection-api-data-analysis-modeling-and-forecasting-29d13e18d06e | The Metropolitan Museum of Art Collection API — Data Analysis, Modeling, and Forecasting | by Elijah Jarocki | Medium

https://github.com/ejarocki/The-Met-API-Data-Analysis/blob/master/The-Met-API-Data-Analysis.pdf | The-Met-API-Data-Analysis/The-Met-API-Data-Analysis.pdf at master · ejarocki/The-Met-API-Data-Analysis


##################
Project Europeana: 

Implement a similar Art Explorer for the art images available from the Project Europeana REST API.

