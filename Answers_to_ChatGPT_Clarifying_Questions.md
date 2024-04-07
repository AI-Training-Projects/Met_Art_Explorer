ChatGPT was used to revise the application, as a demonstration of the power of ChatGPT versus Copilot.
Created On: 2024.04.04
Updated On:

Answer to ChatGPT Clarifying Questions:

I will answer each of your clarifying questions with my answers identified in order.  See below for your training examples. 

1) Could you provide an example of a typical project you're working on, including the specific tasks involved and the desired outcome?

	Q1 Answer: Our first project here: Streamlit App called "Met_Art_Explorer_GPT"

2) Are there any specific challenges or pain points you're encountering in your current projects that you're looking to address through automation and tool development?

	Q2 Answer: We need to improve the usability and GUI layout.  

3) What level of detail are you looking for in the clarification of business process automation? Are you interested in high-level overviews, detailed workflow diagrams, or something in between?

	Q3 Answer:  From the code and enhancements I will give, I want you to generate a workflow diagram.  
	
4) How do you currently manage and document your project requirements, specifications, and implementations? Are there any specific tools or methodologies you prefer to use?

	Q4 Answer: We use VSCode and various plugins to help refine and test code. Python 3 is typically the language, but we also Jupyter Notebook, Streamlit and full stack web app that bundle Python, SQL, JavaScript, HTML, CSS, and other technologies.
	
5) What are your expectations regarding the use of Python, SQL, and Large Language Model (LLM) tools in the context of your projects? Are there any specific functionalities or integrations you're interested in exploring?

	Q5 Answer:  See Q4 Answer for some details.  For a future enhancement, we will also want to integrate the Met_Art_Explorer_GPT to include the Europeana collections using their REST API.  

##########################################################################

Department Fetching:

When fetching department information, would you like to include additional details beyond just the display name and ID, such as descriptions or counts of art pieces in each department?
Random Art Piece Display:

Include 

For each art piece: 

	Art_Piece_Display_Name 
	Art_Piece_Id
	Artist_Name
	Art_Piece_Description
	Museum_Department_Name_(Location)
	Met_Dept_Piece_N_Of_Total

Currently, the application displays a random art piece from the selected department. Are there any specific criteria or filters you'd like to apply when selecting these random art pieces, or is random selection sufficient?

	No cat pictures, if a piece is missing for a random selection, then move on to the next museum piece in that department. If this hard for you to do for the first revision then revert to a cat picture, and we will fix in an update.

Error Handling:

How would you like to handle errors, such as failed API requests or missing data? Should the application display error messages to users, and if so, how should they be presented?

	Add error-handling and report errors in the console, not to the end user.  
	
	Also, add logging to a log_file in a directory named "app_logs", insert logging statements into each function so we know it is entered or exited.  Append all operations to this log_file.

User Interaction:

Are there any additional features or interactions you'd like to incorporate into the application to enhance user engagement or functionality?

	Create a Streamlit Sidebar on the left side for navigating through the different departments.  
	
	Please all Department Buttons in the left-side navigator. 
		
	For each department provide context: 
		Department_Name
		Art_Piece_Count

	Alway display the art piece images in the right-side page.