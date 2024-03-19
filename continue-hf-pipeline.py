import dlt
import json

from huggingface_hub import HfApi


@dlt.resource(table_name="autocompletions")
def resource():
    with open("/Users/oakela/Downloads/autocomplete_nate_continue.jsonl", "r") as file:
        for line in file:
            full_data = json.loads(line)
            if full_data["accepted"]:
                yield {
                    "prompt": full_data["prompt"],
                    "completion": full_data["completion"],
                }


@dlt.destination(batch_size=0, loader_file_format="parquet")
def hf_destination(items, table):
    api = HfApi()
    api.upload_file(
        path_or_fileobj=items,
        path_in_repo=items.split("/")[-1],
        repo_id="oakela/autocompletion_continue_data",
        repo_type="dataset",
    )


pipeline = dlt.pipeline(pipeline_name="continue_data", destination=hf_destination)

load_info = pipeline.run(resource())

print(load_info)
