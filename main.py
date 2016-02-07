#!/usr/bin/python3
"""

"""

import datetime

article_title = str(input("Please enter your title : "))
article_creation_date = str(datetime.datetime.now())
article_category = str(input("Please input your category : "))
article_tags = str(input("Please input your tags : "))
artice_slug = str(article_title.lower().replace(" ","-").encode('ascii',errors='ignore'))
article_creator = str(input("Please enter your name : "))
article_summary = str(input("Please enter your summary : "))
article_header = str(input("Please enter the name of your image : "))

final = "Title: " + article_title + "\nDate: " + article_creation_date + "\nCategory: " + article_category + "\nTags: " + article_tags + "\nSlug: " + artice_slug + "\nAuthors: "+article_creator+"\nSummary: "+article_summary + "\n\n "

article = open(artice_slug + ".md", "w")
article.write(final)
article.close()
