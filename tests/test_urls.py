import requests
import pytest
import glob
import os
import re

# list of notebooks in the gallery
base_path = os.path.dirname(os.path.abspath(__file__))
notebooks = glob.glob(os.path.join(
    base_path, '..', 'docs', 'gallery', 'interactive', '*.ipynb'))


@pytest.mark.parametrize('notebook', notebooks)
def test_urls(notebook):
    '''Test if a url exists and raise an error if not'''
    # load notebook content
    with open(notebook, 'r', encoding='utf-8') as f:
        content = f.read()

    # extract list of links starting with http or www ...
    urls = re.findall(r'(http[s]?://\S+|www\.\S+)', content)
    # ... and ending at the first closing bracket
    urls = [url[:url.find(')')] for url in urls if url.find(')')]

    # check if links exist
    not_found = ''

    for url in urls:
        try:
            site_ping = requests.head(url)
            if site_ping.status_code < 400:
                found = True
            else:
                found = False
        except Exception:
            found = False

        # add feedback if a link does not exist - raise error later
        if not found:
            not_found += f'- {url} is dead\n'

    # raise error if any link does not exist
    if not_found:
        raise ValueError(f'{notebook}:\n{not_found}')
