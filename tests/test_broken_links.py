from pages.broken_links_page import BrokenLinksPage


link = 'https://demoqa.com/broken'
class TestBrokenLinks:


    def test_valid_image(self,page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.is_image_valid(broken_links.valid_image)

    def test_broken_image(self,page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.is_image_not_broken(broken_links.broken_image)

    def test_valid_link(self,page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.check_valid_link()

    def test_broken_linkk(self,page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.check_broken_link()
