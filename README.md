# Blog Website Generator

This is for my coding blogging website. I want to keep a blog consisting of rough progress notes (i.e. journaling) as well as other notes (cheatsheets, notes I take while learning about something). I write my notes in an .md file, and this Python program converts all .md blogs into one HTML website that I can choose to add to my personal portfolio website. 

## How it works (briefly)

* All raw notes are stores as `.md` files in the `notes/` directory.
	* I chose to commit this folder into this respository, for now, as I want to be able to save all my notes as I create them.
	* In the future, if this program becomes sophisticated enough to be useful for others, I'll remove my `notes/` directory (save it somewhere else) so others can add their own `notes/` folder with their own notes. For now if you wish to use this program, just overwrite the `notes/` directory with your own notes.
* I run the `main.py` Python program to generate the website
	* First create the Python virtual environment: `python3 -m venv .`
	* Then activate the virtual environment: `source bin/activate`
	* Install required dependencies: `pip install -r requirements.txt`
	* Run the script! `python main.py`
	* This should convert all `.md` notes from the `notes/` folder into HTML
* The generated website will be in `website/` folder. 
	* Access the website by opening `website/index.html`
	* This folder should not be saved in `git`. It is in `.gitignore` since it's automatically generated.
