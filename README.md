This repository hold nothing except my experimental learning on python, pytests.

implementing small classes and functions to test pytests and build CI Workflows using github actions.

also, connecting it to Docker, Creating a docker image and container for deployment.

The goal was to build unit test ready and integration test ready workflows that function as follows:

  1. On pull request run unit tests
  2. if unit tests succeeds proceed to merge to main
  3. On merging to main, run integration tests
  4. if integration tests succeed proceed to creating a Docker image for the following repo
  5. continue by running the Docker Image in a Container.

This is purely Experimental. Thank you
