

from browser import Browser


class Base_page(Browser):


    def verify_url(self, expected_url):
        url = self.chrom.current_url
        assert url == expected_url, f'Error: Url {url} is different from the expected url {expected_url}'

