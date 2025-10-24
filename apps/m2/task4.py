from bs4 import BeautifulSoup, SoupStrainer

def get_parent(file_path, tag_name):
    # Parse only the desired tag(s)
    strainer = SoupStrainer(tag_name)
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", parse_only=strainer)
    tag = soup.find(tag_name)
    if tag and tag.parent:
        return tag.parent
    return None

if __name__ == "__main__":
    file_path = "large.html"
    tag_name = "p"
    parent = get_parent(file_path, tag_name)
    print(f"Parent of first <{tag_name}> is: {parent.name if parent else 'None'}")