from markdownify import markdownify as md
import pandas as pd
from esiosexplore.requests import indicator_list
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent 
DOCS_DIR = ROOT_DIR.joinpath('docs')

def write_indicators_docs():
    ind_list = indicator_list()
    ind_df = pd.DataFrame(ind_list["indicators"])
    ind_df["description"] = ind_df["description"].apply(md)
    ind_df = ind_df.sort_values("id")
    paragraphs = [
        "# Lista de Indicadores",
        f"generated {datetime.now(tz=timezone.utc).isoformat()}",
    ]
    for index, item in ind_df[["id", "name", "description"]].iterrows():
        paragraphs.append(f"\n## {item['name']}\n\nid: {item.id}\n\n{item.description}")

    with open(DOCS_DIR.joinpath("indicators.md"), "w") as output:
        output.write("\n".join(paragraphs))
