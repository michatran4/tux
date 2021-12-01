# Page generator
import json, markdown, os, shutil
from bs4 import BeautifulSoup
# do not generate new web pages with one open in a browser

def category_tree(category, files, page_footer): # creates pages for each category/directory
    output = ""
    dir_write = os.getcwd() + "/out/" + category # directory to write to
    os.mkdir(dir_write)
    for filename in files:
        filename = filename.replace("\n", "") # could be passed with order.txt, which has newlines
        with open(directory + "-md/" + filename) as file:
            lines = file.readlines() # store so it doesn't act like a scanner, keep entire file for md conversion
            filename = filename.replace(".md", ".html") # write to html, using md file name
            lines.extend(page_footer) # add footer (MD) to the page for conversion
            output += "- [" + lines[0][2:-1] + "](./" + category + "/" + filename + ")\n"
            write = open(dir_write + "/" + filename, "x", encoding="utf-8") # encoding for the penguin
            with open("./build/template.html", encoding="utf-8") as template: # template for each page
                page = template.readlines()
            for i in range(0, len(page)): # find the part to insert page content
                if "[REPLACE]\n" in page[i]:
                    page[i] = markdown.markdown("".join(lines))
            page = '\n'.join(page) # to beautify html requires it to be a string
            soup = BeautifulSoup(page, "html.parser")
            page = soup.prettify()
            write.write(page)
            write.close()
    return output

if __name__ == "__main__":
    try:
        shutil.rmtree('./out') # clean build
    except:
        None
    os.mkdir('./out') # for output files

    with open("./build/categories.json") as file: # all categories/headers
        categories = json.load(file)
    indexMD = ""
    # create indexMD, pages generated along the process
    for category in categories:
        description = ""
        if isinstance(categories[category], dict): # has a description
            headerDescription = categories[category]
            for h in headerDescription:
                header = h
                description = headerDescription[h]
        else:
            header = categories[category]

        # create index.md
        indexMD += "## " + header + "\n"
        if description != "":
            indexMD += description + "\n\n"

        directory = os.getcwd() + "/" + category # create pages from this directory
        file_list = os.listdir(directory + "-md")

        with open("./build/page_footer.md") as footer:
            page_footer = footer.readlines()
        if "order.txt" in os.listdir(directory + "-md"):
            with open(directory + "-md/order.txt") as filenames:
                file_list = filenames.readlines()
        indexMD += category_tree(category, file_list, page_footer) + "\n"

    # index footer
    with open("./build/index_footer.md") as footer:
        index_footer = footer.readlines()
    indexMD += ''.join(index_footer)

    with open("./build/index.html", encoding="utf-8") as template: # index template
        html = template.readlines()
    for i in range(0, len(html)): # insert page content, which is a table of contents
        if "[REPLACE]\n" in html[i]:
            html[i] = markdown.markdown(indexMD)

    html = '\n'.join(html) # beautify requires a string
    soup = BeautifulSoup(html, "html.parser")
    html = soup.prettify()
    write = open("./out/index.html", "x", encoding="utf-8") # encoding for the penguin
    write.write(html) # can't convert entirety to markdown, breaks when detects html lol
    write.close()
    shutil.copyfile("./build/style.css", "./out/style.css")
    shutil.copytree("./img", "./out/img")
