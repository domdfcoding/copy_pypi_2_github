# stdlib
import sys

# 3rd party
import pytest


def test_building(repo_root, docker_client):
	if not (repo_root / "Dockerfile").is_file():
		pytest.skip("Dockerfile not found.")

	print("Building Docker image")

	image, logs = docker_client.images.build(rm=True, path=str(repo_root))
	for line in logs:
		if "stream" in line:
			print(line["stream"], end='')
		sys.stdout.flush()

	print()
