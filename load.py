from argparse import ArgumentParser
from pathlib import Path

from rdflib import Graph
import requests
from requests.exceptions import HTTPError

from graphdb import repository


def get_tern_vocabs():
    response = requests.get(
        "https://graphdb.tern.org.au/repositories/tern_vocabs_core/statements"
    )
    with open("data/tern_vocabs.ttl", "w", encoding="utf-8") as file:
        file.write(response.text)


def get_bdbsa_vocabs():
    response = requests.get(
        "https://graphdb.tern.org.au/repositories/BDBSA_test_core/statements"
    )
    with open("data/bdbsa_vocabs.ttl", "w", encoding="utf-8") as file:
        file.write(response.text)


def main():
    parser = ArgumentParser(
        description="Upload the data in the vocab_files directory to a GraphDB or RDF4J database."
    )
    parser.add_argument(
        "--url",
        dest="url",
        default="http://localhost:7200",
        help="URL of GraphDB or RDF4J base URL [default: http://localhost:7200]",
    )
    parser.add_argument(
        "--repository",
        dest="repository_id",
        default="bdbsa_data_demo",
        help="The GraphDB or RDF4J repository ID [default: bdbsa_data_demo]",
    )
    parser.add_argument(
        "-u",
        "--username",
        dest="username",
        help="The username to use when interfaceing with GraphDB or RDF4J [default: None]",
    )
    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        help="The password to use when interfaceing with GraphDB or RDF4J [default: None]",
    )

    args = parser.parse_args()
    url = args.url
    repository_id = args.repository_id
    username = args.username
    password = args.password

    try:
        repository.create(
            url,
            repository_id,
            "BDBSA Data Demo",
            (username, password),
        )
    except HTTPError:
        # Repository already exists, probably.
        pass

    # Load additional vocabs
    get_tern_vocabs()
    get_bdbsa_vocabs()

    data_files = Path("data")
    files = list(data_files.glob("**/*.ttl"))

    graph = Graph()
    for file in files:
        graph.parse(file, format="turtle")

    data = graph.serialize(format="turtle", encoding="utf-8")

    repository.insert(
        url,
        repository_id,
        data,
        "text/turtle",
        "<https://linked.data.gov.au/dataset/bdbsa>",
        (username, password),
    )


if __name__ == "__main__":
    main()
