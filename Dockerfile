FROM tecktron/python-bjoern
LABEL maintainer="Brian Wilson <brian@wildsong.biz>"
LABEL version="2023-04-27"
LABEL biz.wildsong.name="bjoern-template"


# Refer to https://github.com/Tecktron/docker-python-bjoern
# Keep in mind this is a Debian + Python based image

# Add flask and anything else you need
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/
COPY app .
COPY log.ini .

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/run.sh"]
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl --fail http://localhost:80/ || exit 1