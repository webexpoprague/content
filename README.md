# WebExpo Content

WebExpo Content extraction from website in MD format. Simple python 3.13 script to get WebExpo data in MD format for broader use.

## Install

```bash
git clone git@github.com:webexpoprague/content.git webexpo_content
cd webexpo_content
python3.13 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt 
```

### Usage

Run the data scrape in markdown format as below:

```bash
python3.13 -m venv myenv
python3 collate_content.py
```

Then use the contents from 'output' as you please.
