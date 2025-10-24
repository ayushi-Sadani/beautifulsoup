from bs4 import BeautifulSoup, SoupStrainer

def get_tag(file_path, tag_name):
    # Parse only the specified tag type
    strainer = SoupStrainer(tag_name)
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", parse_only=strainer)
    return soup.find_all(tag_name)

if __name__ == "__main__":
    file_path = "large.html"   # test with a large HTML/XML file
    tag_name = "a"
    tags = get_tag(file_path, tag_name)
    print(f"Found {len(tags)} <{tag_name}> tags")
    for t in tags[:10]:  # print only first 10 for sanity
        print(t)