from dataclasses import dataclass
import json
from pyld import jsonld
import pprint

@dataclass
class Dataset:
    uri: str
    title: dict
    description: dict
    publisherId: str
    accessRights: str

DATA_FILE_PATH="./data.jsonld"
#DATA_FILE_PATH="./raw.jsonld"  # alternative 2

def main():
    with open(DATA_FILE_PATH, "r") as json_file, open("./frame.jsonld", "r") as jsonld_frame_file:
        # Transform JSON-LD to easily consumable structure
        json_data = json.load(json_file)  # Dataset description in JSON-LD/RDF
        jsonld_frame = json.load(jsonld_frame_file)
        framed_json = jsonld.frame( # changes structure of JSON data according to frame.jsonld
            jsonld.expand(json_data),
            jsonld_frame
        )

        # Map to Dataset Class
        dataset = Dataset(
            uri = framed_json.get("Dataset.uri"),
            title = framed_json.get("Dataset.title"),
            description = framed_json.get("Dataset.description"),
            publisherId = framed_json.get("Dataset.publisher"),
            accessRights = framed_json.get("Dataset.accessRights")
        )

        print_info(dataset)

def print_info(dataset):
    print("*** Dataset info ***")
    print(f"  URI: {dataset.uri}")
    print("  Title:")
    for lang in dataset.title:
        print(f"   {lang}: {dataset.title[lang]}")
    print("  Description:")
    for lang in dataset.description:
        print(f"   {lang}: {dataset.description[lang]}")
    print(f"  Publisher ID: {dataset.publisherId}")
    print(f"  Access rights: {dataset.accessRights}")


if __name__ == "__main__":
    main()
