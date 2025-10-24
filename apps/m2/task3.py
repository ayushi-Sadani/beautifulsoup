from bs4 import BeautifulSoup, SoupStrainer

def get_children(file_path, parent_tag):
    # Parse only the parent and its children
    strainer = SoupStrainer(parent_tag)
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", parse_only=strainer)
    parent = soup.find(parent_tag)
    if not parent:
        return []
    return [child for child in parent.children if child.name is not None]

if __name__ == "__main__":
    file_path = "large.html"
    parent_tag = "div"
    children = get_children(file_path, parent_tag)
    print(f"Children of <{parent_tag}>:")
    for c in children[:10]:
        print(c.name)