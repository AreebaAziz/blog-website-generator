main_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes</title>
</head>
<body>
    <h1>My Notes</h1>
    <ul>
    	{notes_list}
    </ul>
</body>
</html>
"""

notes_list_item = "<li><a href=\"notes/{page_name}.html\">{title}</a></li>"

note_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes - {title}</title>
</head>
<body>
    {body}
</body>
</html>
"""

# title = "Note 01"
# content = content_in_html
