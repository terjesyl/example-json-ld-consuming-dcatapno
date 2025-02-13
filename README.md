# Consuming RDF as JSON-LD for a system specific data structure

Requires: `PyLD` - [JSON-LD Processor](https://github.com/digitalbazaar/pyld) from digitalbazaar

## Scenario

- You want to consume RDF data which is defined according to DCAT-AP-NO.
- You have a custom data model as defined in the Python Class `Dataset` (in `main.py`).
- You need to map from the RDF data (in JSON-LD format) to the data class.

For this purpose JSON-LD Framing can be used, by running

```python
framed_json = jsonld.frame(jsonld.expand(json_data), jsonld_frame)
```

the JSON-LD is then restructured to fit to the Dataset-class.

## Notes

The data in `data.jsonld` is assumed to come from an external resource, and is assumed to contain only one instance of `dcat:Dataset`.

The frame in `frame.jsonld` is defined by the consumer, as it is tied to the data structure/data models used in the application (`main.py`).

`raw.json` is unused, but shown as an example of how fetched JSON-LD data containing `dcat:Dataset` might look like. You can use this as `json_file` instead, and be able to parse it to the Dataset-structure, with the help of framing, just uncomment

```python
DATA_FILE_PATH="./raw.jsonld"
```

## To run

### Create venv

```
python -m venv .venv
```

### Install PyLD

```
pip install PyLD
```

### Run

```
python main.py
```
