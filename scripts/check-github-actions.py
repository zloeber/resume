#!/usr/bin/env python3

import re
import sys

import requests
import yaml

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/releases/latest"


def get_latest_version(owner, repo):
    try:
        response = requests.get(GITHUB_API_URL.format(owner=owner, repo=repo))
        response.raise_for_status()
        data = response.json()
        return data.get("tag_name", "Unknown")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest version for {owner}/{repo}: {e}")
        return "Unknown"


def parse_workflow_file(workflow_file_path):
    with open(workflow_file_path, 'r') as file:
        try:
            workflow = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return []

    actions = []
    jobs = workflow.get('jobs', {})
    for job in jobs.values():
        steps = job.get('steps', [])
        for step in steps:
            if 'uses' in step:
                uses_value = step['uses']
                match = re.match(r'([^@]+)@(.+)', uses_value)
                if match:
                    action = match.group(1)
                    version = match.group(2)
                    actions.append((action, version))
    return actions


def main(workflow_file_path):
    actions = parse_workflow_file(workflow_file_path)

    for action, current_version in actions:
        owner_repo = action.replace('https://github.com/', '').split('/')
        if len(owner_repo) == 2:
            owner, repo = owner_repo
            latest_version = get_latest_version(owner, repo)
            if latest_version == "Unknown":
                print(f"Could not determine the latest version for {action}")
            elif current_version != latest_version:
                print(
                    f"Action {action}: Current version {current_version} is not the latest. Latest version is {latest_version}.")
            else:
                print(
                    f"Action {action}: Current version {current_version} is the latest.")
        else:
            print(f"Skipping unsupported action format: {action}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_action_versions.py <workflow_file_path>")
        sys.exit(1)

    workflow_file_path = sys.argv[1]
    main(workflow_file_path)
