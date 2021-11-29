# Page generator
import json, markdown, os, shutil
from bs4 import BeautifulSoup
# do not generate new web pages with one open in a browser

def category_tree(category, files, footer):
    output = ""
    dir_write = os.getcwd() + "/out/" + category # directory to write to
    os.mkdir(dir_write)
    for filename in files:
        filename = filename.replace("\n", "") # could be passed with order.txt, which has newlines
        with open(directory + "-md/" + filename) as file:
            lines = file.readlines() # store so it doesn't act like a scanner, keep entire file for md conversion
            filename = filename.replace(".md", ".html")
            lines.extend(footer)
            output += "- [" + lines[0][2:-1] + "](./" + category + "/" + filename + ")\n"
            write = open(dir_write + "/" + filename, "x")
            page = markdown.markdown("".join(lines))
            soup = BeautifulSoup(page, "html.parser")
            page = soup.prettify()
            write.write(page)
            write.close()
    return output

if __name__ == "__main__":
    try:
        shutil.rmtree('./out')
    except:
        None
    os.mkdir('./out') # for output files

    with open("./build/categories.json") as file:
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

        directory = os.getcwd() + "/" + category
        file_list = os.listdir(directory + "-md")

        with open("./build/page_footer.md") as page_footer:
            footer = page_footer.readlines()
        if "order.txt" in os.listdir(directory + "-md"):
            with open(directory + "-md/order.txt") as filenames:
                file_list = filenames.readlines()
        indexMD += category_tree(category, file_list, footer) + "\n"

    # index footer
    indexMD += """### About
- I am [Michael Tran](https://ttrraann.com), a junior in high school.
- I made this site as an archive for the most important things I have learned on GNU/Linux, hence why the pages are lacking extraneous options I don't use.
- I included systemd because I use Arch Linux often.
"""
    indexMD += ''.join(footer)

    dir_write = os.getcwd() + "/out/"
    with open("./build/index.html", encoding="utf-8") as template:
        html = template.readlines()
    for i in range(0, len(html)):
        if "[REPLACE]\n" in html[i]:
            html[i] = markdown.markdown(indexMD)

    html = '\n'.join(html)
    soup = BeautifulSoup(html, "html.parser")
    html = soup.prettify()
    write = open("./out/index.html", "x", encoding="utf-8")
    write.write(html) # can't convert entirety to markdown, breaks when detects html lol
    write.close()
    shutil.copyfile("./build/style.css", "./out/style.css")
