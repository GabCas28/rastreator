# Elastic Search with Django

This project makes use of the [Python Elasticsearch Client](https://elasticsearch-py.readthedocs.io/en/v7.12.0/#python-elasticsearch-client)

It uses a [sample data](https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json) automatically generated. It was taken from the following [elastic search tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-index.html).

## Installation

To run the project you will need to install Docker first. Then, download the project and run the command `docker-compose up` from its root folder.

## Usage

Once the project is up and running, just visit [http://localhost:8000](http://localhost:8000) to interact with the interface.

You can search from the top-right form, using a [Lucene syntax](https://www.elastic.co/guide/en/kibana/current/lucene-query.html#lucene-query) on your queries.
