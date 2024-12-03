import os
import urllib.parse

os.remove("styles_tagicons_list.css")


with open('styles_tagicons_list.css', 'a') as f:
    for subdir, dirs, files in os.walk("icons/tags"):
        for filename in files:
            tagname=filename.replace(".webp","")
            f.write('li.flex[data-tag-name="{}"] {{\n'.format(tagname))
            f.write('     background-image: url("https://raw.githubusercontent.com/midpark/DarkRetro2K/main/icons/tags/{}.webp");\n'.format(tagname))
            f.write('}\n')
            f.write('\n')
            f.write('li.ui-menu-item[data-autocomplete-value="{}"] .ui-menu-item-wrapper {{\n'.format(tagname))
            f.write('    background-image: url("https://raw.githubusercontent.com/midpark/DarkRetro2K/main/icons/tags/{}.webp");\n'.format(tagname))
            f.write('}\n')
            f.write('\n')

            f.write('a.dtext-link.dtext-wiki-link[href="/wiki_pages/{}"] {{\n'.format(urllib.parse.quote(tagname)))
            f.write('    padding-left: 20px;\n    background-image: url("https://raw.githubusercontent.com/midpark/DarkRetro2K/main/icons/tags/{}.webp");\n    background-size: contain;\n    background-repeat:no-repeat;'.format(tagname))
            f.write('\n}\n')

