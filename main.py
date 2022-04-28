import sys

from bs4 import BeautifulSoup
import markdownify
from markdowndatamodel import MarkdowndataModel
import os


def get_all_file_path(direc):
    file_paths = list()
    for root, dirs, files in os.walk(direc):
        for file in files:
            if file.endswith('.html'):
                file_paths.append(os.path.abspath(os.path.join(root, file)))
    return file_paths


def get_date_description_info(line):
    # Break the line
    date_published, date_modified, description = "", "", ""
    date_info = line.split("datePublished")[1]
    date_info = date_info.split("inLanguage")[0]
    line_values = date_info.split(",")
    date_published = line_values[0].split(":\"")[1].split("\"")[0]
    for val in line_values[1:]:
        if "dateModified" in val:
            date_modified = val.split(":\"")[1].split("\"")[0]
        if "description" in val:
            description = val.split(":\"")[1].split("\"")[0]
    return date_published, date_modified, description


def get_file_name(file_path):
    split_val = "C:\\Users\\barad\\CodeSpace\\websites\\androidmonks.com\\"
    val = file_path.split(split_val)[1]
    print(val)
    val = val.replace("\\","-")
    print(val)
    return val


def convert_to_md(output_dir, file_path_list):
    for file_path in file_path_list:
        print(file_path)
        file_name = get_file_name(file_path)
        # get file_name
        with open(file_path, 'r', encoding="utf-8") as f:
            html = f.read()

        # Create markdown
        text = markdownify.markdownify(html, heading_style="ATX")
        with open(f"{output_dir}/{file_name}.md", 'w', encoding="utf-8") as write_file:
            write_file.write(text)

        # Clean up the text before sending to md
        temp_file = "temp.txt"

        markdown_data = MarkdowndataModel()
        # Markdown model
        lines = list()
        with open(f"{output_dir}/{file_name}.md", "r", encoding="utf-8") as input_file:
            with open(temp_file, "w", encoding="utf-8") as output:
                file_start = False
                for line in input_file:
                    if "datePublished" in line.strip("\n"):
                        print("Date published")
                        date_published, date_modified, description = get_date_description_info(line)
                    if line.strip("\n").startswith('# '):
                        file_start = True
                        doc_title = line
                    if line.strip("\n").startswith('### Leave a Comment'):
                        file_start = False
                    if file_start:
                        lines.append(line)
                markdown_data.set_model_info(doc_title, description, date_published, date_modified, "")
                output_lines = ''.join(lines)
                output_lines = markdown_data.get_model_info_as_text() + output_lines
                output.write(output_lines)
                # Add important markdown information
        os.replace('temp.txt', f"{output_dir}/{file_name}.md")


if __name__ == '__main__':
    directory = "C:/Users/barad/CodeSpace/websites/"
    # Get all the file paths that have to converted to a md file here
    file_paths = get_all_file_path(directory)
    print(file_paths)
    convert_to_md("C:/Users/barad/CodeSpace/websites/outputdir", file_paths)
# Create a Next.JS POST file

# Save and Exit
