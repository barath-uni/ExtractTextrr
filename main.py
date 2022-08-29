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
    print("BEFORE")
    print(file_path)
    val = os.path.split(file_path)[1]
    val = val.replace(".html","")
    val = val.replace(" ","_")
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
        with open(f"{output_dir}/{file_name}.md", 'w+', encoding="utf-8") as write_file:
            write_file.write(text)

        # Clean up the text before sending to md
        temp_file = "temp.txt"

        markdown_data = MarkdowndataModel()
        doc_title = "TITLE HERE"
        description, date_published, date_modified = "DESCRIPTION", "2022-08-08", "2022-08-08"
        # Markdown model
        lines = list()
        with open(f"{output_dir}/{file_name}.md", "r", encoding="utf-8") as input_file:
            with open(temp_file, "w", encoding="utf-8") as output:
                markdown_data.set_model_info(doc_title, description, date_published, date_modified, "")
                output_lines = ''.join(input_file)
                output_lines = markdown_data.get_model_info_as_text() + output_lines
                output.write(output_lines)
                # Add important markdown information
        os.replace('temp.txt', f"{output_dir}/{file_name}.md")


if __name__ == '__main__':
    directory = "/home/barath/blogwriter/AutoBlogWriter/output"
    # Get all the file paths that have to converted to a md file here
    file_paths = get_all_file_path(directory)
    print(file_paths)
    if not os.path.exists("/home/barath/blogwriter/AutoBlogWriter/outputdir"):
        os.makedirs("/home/barath/blogwriter/AutoBlogWriter/outputdir")
    convert_to_md("/home/barath/blogwriter/AutoBlogWriter/outputdir", file_paths)
# Create a Next.JS POST file

# Save and Exit
