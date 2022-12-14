import os
import sys
from pathlib import Path
from markdown import markdown

import template

NOTES_DIR = "notes/"
WEBSITE_DIR = "website/"
NOTE_EXTENSION = ".md"
TARGET_EXTENSION = ".html"

def create_html_file_from_md_file(md_file_location):
	# Read .md file
	content_md = Path(md_file_location).read_text()

	# Convert .md content to .html content
	content_html = markdown(content_md, extensions=['fenced_code'])

	# Generate html file location given the md source location
	html_target_location = generate_html_target_location(md_file_location)
	html_target_location = html_target_location.replace(NOTE_EXTENSION, TARGET_EXTENSION)

	# Write .html content to target file location, create dirs if needed
	dirs = os.path.split(html_target_location)[0]
	if dirs:
		Path(dirs).mkdir(parents=True, exist_ok=True)
	Path(html_target_location).write_text(content_html)

def check_if_note(filepath):
	return filepath.endswith(NOTE_EXTENSION)

def generate_html_target_location(md_file_location):
	return md_file_location.replace(NOTES_DIR, WEBSITE_DIR, 1)

def create_index_html(website_root=WEBSITE_DIR):
	# Create root layer based on given `website_root`
	toplevel = next(os.walk(website_root))
	root = toplevel[0]
	subdirs = toplevel[1]
	files = toplevel[2]
	notes_list = ""
	for subdir in subdirs:
		item = template.subdir_item.format(title=subdir)
		notes_list += item

	for file in files:
		if (file != "index.html"):
			item = template.file_item.format(title=file)
			notes_list += item

	page_html = template.index_page.format(page_title=root, notes_list=notes_list)
	Path(os.path.join(root, "index.html")).write_text(page_html)

	for subdir in subdirs:
		create_index_html(os.path.join(root, subdir))

# `md_source` can be either file or dir
def main(md_source=NOTES_DIR, website_root=WEBSITE_DIR):
	md_file_location = ""
	html_target_location = ""

	if os.path.isfile(md_source):
		create_html_file_from_md_file(md_source)
	else:
		for root, subdirs, files in os.walk(md_source):
			for file in files:
				filepath = os.path.join(root, file)
				if (check_if_note(filepath)):
					create_html_file_from_md_file(filepath)
	
	create_index_html(website_root)


args_len = len(sys.argv)
if (args_len > 3):
	print("Error - too many arguments")
elif (args_len == 3):
	main(sys.argv[1], sys.argv[2])
elif (args_len == 2):
	main(sys.argv[1])
else:
	main()
