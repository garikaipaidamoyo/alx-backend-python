#!/usr/bin/env python3

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


# Add a new test class for Task 9
@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ],
)
class TestIntegrationGithubOrgClientWithFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mock the requests.get method to return org_payload
        cls.org_patcher = patch('requests.get', return_value=cls.org_payload)
        cls.org_patcher.start()

        # Initialize the GithubOrgClient
        cls.client = GithubOrgClient("test")

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher after all tests are finished
        cls.org_patcher.stop()

    def test_public_repos(self):
        # Ensure public_repos returns the expected results based on fixtures
        repos = self.client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        # Test public_repos with the argument license="apache-2.0"
        repos = self.client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", {
            "login": "google"
        }),
        ("abc", {
            "login": "abc"
        }),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, org_payload, mock_get_json):
        mock_get_json.return_value = org_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org_payload)

    @patch(
        'test_client.GithubOrgClient.org',
        new_callable=PropertyMock,
        return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos_url(self, mock_org):
        client = GithubOrgClient('google')
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({
            "name": "repo1"
        }, "my_license", True),
        ({
            "name": "repo2"
        }, "my_license", False),
    ])
    @patch(
        'test_client.GithubOrgClient.org',
        new_callable=PropertyMock,
        return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    @patch('client.get_json')
    def test_has_license(self, repo, license_key, expected_result,
                         mock_get_json, mock_org):
        mock_get_json.return_value = [repo]
        client = GithubOrgClient("google")
        result = client.has_license(license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            {
                "login": "google"
            },
            [
                {
                    "name": "repo1",
                    "license": {
                        "key": "my_license"
                    }
                },
                {
                    "name": "repo2",
                    "license": {
                        "key": "other_license"
                    }
                },
                {
                    "name": "repo3"
                },
            ],
            ["repo1", "repo2", "repo3"],
            ["repo1"],
        ),
        (
            {
                "login": "abc"
            },
            [
                {
                    "name": "repo4",
                    "license": {
                        "key": "my_license"
                    }
                },
                {
                    "name": "repo5",
                    "license": {
                        "key": "other_license"
                    }
                },
                {
                    "name": "repo6"
                },
            ],
            ["repo4", "repo5", "repo6"],
            ["repo4"],
        ),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @patch('requests.get')
    def setUp(self, mock_requests_get):
        responses = [
            Mock(json=lambda: self.org_payload),
            Mock(json=lambda: self.repos_payload)
        ]
        mock_requests_get.side_effect = responses

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        client = GithubOrgClient('google')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
