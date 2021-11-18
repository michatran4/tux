import json, markdown, os

def category_tree(category, files):
    output = ""
    for filename in files:
        filename = filename.replace("\n", "")
        with open(directory + "-md/" + filename) as file:
            lines = file.readlines()
            output += "- [" + lines[0][2:-1] + "](./" + category + "/" + filename + ")\n"
            # TODO build pages and make directories
    return output

if __name__ == "__main__":
    try:
        os.rmdir('./out')
    except:
        None

    # os.mkdir('./out')

    with open("./build/categories.json") as file:
        categories = json.load(file)
    indexMD = "# 🐧 TUX'S COMMANDS\n"

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
            indexMD += description + "\n"

        directory = os.getcwd() + "/" + category
        file_list = os.listdir(directory + "-md")
        if "order.txt" in os.listdir(directory + "-md"):
            with open(directory + "-md/order.txt") as filenames:
                file_list = filenames.readlines()
        indexMD += category_tree(category, file_list) + "\n"

    indexMD += """### About
- I am [Michael Tran](https://ttrraann.com), a junior in high school.
- I made this site as an archive for the most important things I have learned on GNU/Linux, hence why the pages are lacking extraneous options I don't use.
- I included systemd because I use Arch Linux often.

---

All site content is in the [Public Domain](http://unlicense.org/)."""

    print(indexMD)
    #print(markdown.markdown(indexMD))
