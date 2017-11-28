"""Tests for server routes"""
import unittest
import server


class routeTests(unittest.TestCase):
    """Tests for my server routes"""

    def setUp(self):
        """Code to run before every test"""
        # Creating a test client similar to our server
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    # Test whether the right (home)page loads upon running the server.
    def test_homepage(self):
        """Test for opening homepage"""

        result = self.client.get("/")
        self.assertIn("Welcome to the", result.data)

    # Test whether the search page loads correctly
    # Note: just the page-load tested here, not the button-click
    # def test_searchpage(self):
    #     """Test for opening searchpage"""

    #     result = self.client.get("/choose-search")
    #     self.assertIn("Search your favorite", result.data)

    # Test navigation of page by giving dummy input
    # Note: This is not button-click tests
    def test_searchresults(self):
        """Test for opening search results"""

        search_info = {'city': "San Jose", 'state': "California",
                       'radius': "15"}
        result = self.client.post("/search-hike", data=search_info,
                                  follow_redirects=True)

        self.assertIn("The results", result.data)
        self.assertNotIn("there are no hikes", result.data)


if __name__ == "__main__":
    unittest.main()
