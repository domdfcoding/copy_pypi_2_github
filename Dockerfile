FROM python:slim
LABEL "maintainer"="Dominic Davis-Foster <dominic@davis-foster.co.uk>"

ADD . /copy_pypi_2_github
RUN python3 -m pip install /copy_pypi_2_github
ENV GITHUB_TOKEN $GITHUB_TOKEN

ENTRYPOINT ["/copy_pypi_2_github/copy_pypi_2_github/action.py"]
