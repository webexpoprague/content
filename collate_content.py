import os
import requests

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def process_sessions(sessions_file, output_file):
    if not os.path.exists(sessions_file):
        print(f"{sessions_file} does not exist.")
        return

    with open(sessions_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for url in urls:
            markdown_url = f"{url}?feature=markdown"
            print(f"Fetching session URL: {markdown_url}")
            content = fetch_content(markdown_url)
            out_f.write(content + "\n\n")

    print(f"Sessions data written to {output_file}")

def process_pages(pages_file, output_file):
    if not os.path.exists(pages_file):
        print(f"{pages_file} does not exist.")
        return

    with open(pages_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for url in urls:
            markdown_url = f"{url}?feature=markdown"
            print(f"Fetching page URL: {markdown_url}")
            content = fetch_content(markdown_url)

            # Modify headings: replace "Session" with "Page"
            content = content.replace("# Session", "# Page")
            content = content.replace("## Session URL", "## Page URL")

            out_f.write(content + "\n\n")

    print(f"Site pages data written to {output_file}")

def main():
    sessions_file = 'sessions.txt'
    pages_file = 'pages.txt'
    sessions_output = 'sessions-data.md'
    pages_output = 'site-data.md'

    process_sessions(sessions_file, sessions_output)
    process_pages(pages_file, pages_output)

if __name__ == "__main__":
    main()
