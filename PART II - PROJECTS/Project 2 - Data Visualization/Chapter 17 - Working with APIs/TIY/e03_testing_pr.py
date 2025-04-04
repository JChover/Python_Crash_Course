# 17-03 Testing python_repos.py - e03_testing_pr.py
import unittest
import requests

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        """Set up the API call and parse the JSON response."""
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.response = requests.get(self.url, headers=self.headers)
        self.response_dict = self.response.json()

    def test_status_code(self):
        """Assert that the API returns status code 200."""
        self.assertEqual(self.response.status_code, 200, "Status code is not 200.")

    def test_total_count(self):
        """
        Assert that the total count of repositories is a positive number.
        You can adjust the threshold depending on your expectations.
        """
        total_count = self.response_dict.get('total_count', 0)
        self.assertGreater(total_count, 0, "Total count should be greater than 0.")

    def test_items_returned(self):
        """
        Assert that the 'items' key contains the expected number of repository entries.
        By default, GitHub returns 30 repositories per page unless modified.
        """
        repo_items = self.response_dict.get('items', [])
        # Check that it's a list and that we received 30 items.
        self.assertIsInstance(repo_items, list, "'items' should be a list.")
        self.assertEqual(len(repo_items), 30, "Expected 30 repository items to be returned.")

    def test_repository_fields(self):
        """
        Verify that each repository item contains the expected keys.
        This checks the first repository as a representative sample.
        """
        repo_items = self.response_dict.get('items', [])
        if not repo_items:
            self.fail("No repositories returned to test repository fields.")
        repo = repo_items[0]
        expected_keys = ['name', 'owner', 'stargazers_count', 'html_url', 'created_at', 'updated_at', 'description']
        for key in expected_keys:
            self.assertIn(key, repo, f"Key '{key}' not found in repository item.")

        # Additionally, check that 'owner' is a dict and has the key 'login'.
        self.assertIsInstance(repo['owner'], dict, "'owner' should be a dictionary.")
        self.assertIn('login', repo['owner'], "Owner should have a 'login' key.")

if __name__ == '__main__':
    unittest.main()
