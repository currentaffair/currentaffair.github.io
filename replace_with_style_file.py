from bs4 import BeautifulSoup
import os
import glob

def modify_html_style(input_file, output_file, css_path):
    """
    Modifies an HTML file by removing existing style tags and adding a link to external CSS.
    
    Args:
        input_file (str): Path to the input HTML file
        output_file (str): Path to save the modified HTML file
        css_path (str): Path to the CSS file to be linked
    """
    # Read the HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove all style tags
    for style_tag in soup.find_all('style'):
        style_tag.decompose()
    
    # Remove all link tags that reference stylesheets
    for link_tag in soup.find_all('link', rel='stylesheet'):
        link_tag.decompose()
    
    # Create new link tag for external CSS
    new_link = soup.new_tag('link')
    new_link['rel'] = 'stylesheet'
    new_link['type'] = 'text/css'
    new_link['href'] = css_path
    
    # Add the new link tag to head
    head = soup.find('head')
    if head is None:
        # Create head tag if it doesn't exist
        head = soup.new_tag('head')
        if soup.html is None:
            # Create html tag if it doesn't exist
            html = soup.new_tag('html')
            soup.append(html)
        soup.html.insert(0, head)
    
    head.append(new_link)
    
    # Save the modified HTML
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))


# Example usage
if __name__ == "__main__":
    editorials_file = "./2025/January/22-01-25/editorials/article1.html"
    quick_facts_file = "./2025/January/22-01-25/quick_facts/article1.html"
    editorials_style_path = '../../../../editorials_style.css'
    quick_facts_style_path ='../../../../quick_facts_style.css' 
    print(" making changes in the all the files of the January")
    
    dates = os.listdir('./2025/February/')
    print(dates)
    dates_folders  =  []
    for date in dates:
        temp_list = editorials_file.split("/")
        temp_list[3] = date
        folder_name = "/".join(temp_list[:-1]) 
        dates_folders.append(folder_name)

    for date in dates:
        temp_list = quick_facts_file.split("/")
        temp_list[3] = date
        folder_name = "/".join(temp_list[:-1])
        dates_folders.append(folder_name)
    
    all_html_files = []
    for folder in dates_folders:
        files = glob.glob(f"{folder}/*.html")
        all_html_files.extend(files)

    for html_file in all_html_files:
        print("working with html file " , html_file)
        if 'editorials' in html_file:
            style_path = editorials_style_path
            print("style sheet for the file is ", editorials_style_path)
        else:
            print("style sheet for the file is ", quick_facts_style_path)
            style_path = quick_facts_style_path 

     
        modify_html_style(
            input_file=html_file,
            output_file=html_file,
            css_path=style_path
        )
