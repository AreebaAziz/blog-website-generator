from pathlib import Path
from markdown import markdown

from template import main_page, note_page, notes_list_item

page = ""
content_md = Path('notes/notes-01.md').read_text()
content_html = markdown(content_md, extensions=['fenced_code'])

notes_list_item = notes_list_item.format(page_name="note_01", title="Note 01")
note_page = note_page.format(title="Note 01", body=content_html)
main_page = main_page.format(notes_list=notes_list_item) # todo replace with list of items

main_page_f = open("website/index.html", "w")
main_page_f.write(main_page)
main_page_f.close()

note_page_f = open("website/notes/note_01.html", "w")
note_page_f.write(note_page)
note_page_f.close()