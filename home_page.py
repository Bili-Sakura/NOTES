import os
import streamlit as st
import re


def convert_image_paths(markdown_content, base_dir):
    """
    Converts invalid image paths in Markdown content to valid paths.

    Parameters:
    - markdown_content (str): The content of the Markdown file.
    - base_dir (str): The base directory where images are stored.

    Returns:
    - str: The updated Markdown content with valid image paths.
    """
    # Pattern to find image markdown syntax
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"

    def replace_invalid_path(match):
        alt_text = match.group(1)
        img_path = match.group(2)

        # Check if the image path is valid
        if not os.path.isfile(img_path):
            # Construct the new valid path
            new_path = os.path.join(base_dir, os.path.basename(img_path))
            if os.path.isfile(new_path):
                return f"![{alt_text}]({new_path})"
            else:
                return f"![{alt_text}](invalid_path/{os.path.basename(img_path)})"
        return match.group(0)

    # Replace all invalid paths in the Markdown content
    updated_content = re.sub(image_pattern, replace_invalid_path, markdown_content)

    return updated_content


# Example usage:
markdown_file_path = (
    "./Bilibili_Course/LLM/course_notes/Markdown/【序】五分钟了解大语言模型.md"
)
base_directory = "./Bilibili_Course/LLM/course_notes/assets"

# Read the Markdown file
with open(markdown_file_path, "r", encoding="utf-8") as file:
    original_content = file.read()

# Convert image paths
updated_content = convert_image_paths(original_content, base_directory)

# Optionally write the updated content back to a file
with open("updated_markdown_file.md", "w", encoding="utf-8") as file:
    file.write(updated_content)

st.markdown(updated_content, unsafe_allow_html=True)


# st.set_page_config(page_title="Sakura Notes Home Page", page_icon=None, layout="wide")
# st.title("Sakura Notes Home Page")
# st.image("./assets/sakura.png")
# tab_profile, tab_llm_0, tab_llm_1 = st.tabs(["Profile", "LLM_0", "LLM_1"])


# with tab_llm_0:
#     with open(
#         "./Bilibili_Course/LLM/course_notes/Markdown/【序】五分钟了解大语言模型.md",
#         "r",
#         encoding="utf-8",
#     ) as f:
#         content = f.read()
#         st.markdown(content, unsafe_allow_html=True)
