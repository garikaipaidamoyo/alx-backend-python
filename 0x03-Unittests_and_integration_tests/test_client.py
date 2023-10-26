#!/usr/bin/env python3

# test_client.py

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, mock_get_json):
        client = GithubOrgClient("google")
        org = client.org
        self.assertEqual(org, {"login": "google"})

    @patch('client.get_json',
           return_value=[{
               "name": f"repo{i}"
           } for i in range(1, 4)])
    def test_public_repos(self, mock_get_json):
        client = GithubOrgClient("google")
        repos = client.public_repos()
        expected_repos = [f"repo{i}" for i in range(1, 4)]
        self.assertEqual(repos, expected_repos)

    @patch('client.get_json',
           return_value=[{
               "name": f"repo{i}"
           } for i in range(1, 4)])
    def test_public_repos_url(self, mock_get_json):
        client = GithubOrgClient("google")
        repos = client.public_repos()
        expected_repos = [f"repo{i}" for i in range(1, 4)]
        self.assertEqual(repos, expected_repos)

    def test_has_license(self):
        client = GithubOrgClient("google")
        repo = {"license": {"key": "my_license"}}
        self.assertTrue(client.has_license(repo, "my_license"))


class TestIntegrationGithubOrgClient(unittest.TestCase):

    @patch('client.requests.get',
           side_effect=[
               unittest.mock.Mock(json=lambda: {"login": "google"}),
               unittest.mock.Mock(json=lambda: [{
                   "name": f"repo{i}"
               } for i in range(1, 4)])
           ])
    def test_public_repos(self, mock_requests_get):
        client = GithubOrgClient("google")
        repos = client.public_repos()
        expected_repos = [f"repo{i}" for i in range(1, 4)]
        self.assertEqual(repos, expected_repos)


if __name__ == '__main__':
    unittest.main()
