import markdown

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

if __name__ == "__main__":
    markdown_text = input("Enter the Markdown formatted text: ")
    html_text = markdown_to_html(markdown_text)
    print("HTML Output:")
    print(html_text)