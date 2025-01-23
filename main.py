from dataclasses import dataclass
import json

@dataclass
class Dataset:
    uri: str
    title: dict
    description: dict
    publisherId: str
    accessRights: str


def main():
    with open("./data.jsonld", "r") as f:
        json_data = json.load(f)
        dataset = Dataset(
            uri = json_data.get("Dataset.uri"),
            title = json_data.get("Dataset.title"),
            description = json_data.get("Dataset.description"),
            publisherId = json_data.get("Dataset.publisher"),
            accessRights = json_data.get("Dataset.accessRights")
        )

        print(dataset.uri)

        print(f"Title: {dataset.title}")

        for lang in dataset.title:
            print(dataset.title[lang])

        for lang in dataset.description:
            print(dataset.description[lang])


if __name__ == "__main__":
    main()
