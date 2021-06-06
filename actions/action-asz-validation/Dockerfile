FROM python

LABEL "maintainer" = "Matt Briggs <mabrigg@microsoft.com>"

COPY requirements.txt /usr/local/bin/requirements.txt
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN pip install -r /usr/local/bin/requirements.txt

ENTRYPOINT ["bash", "/usr/local/bin/entrypoint.sh"]
