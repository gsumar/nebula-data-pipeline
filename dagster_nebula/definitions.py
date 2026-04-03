"""
Dagster definitions module - the "glue" that ties everything together.
This module loads all assets and resources and creates the Dagster job definitions.
"""

from dagster import Definitions, load_assets_from_modules
from dagster_nebula.assets import ingestion, processing

# Load all assets from the asset modules
all_assets = load_assets_from_modules(
    [ingestion, processing],
    group_name="nebula_assets"
)

# Create the Definitions object
defs = Definitions(
    assets=all_assets,
    # Resources can be added here as needed
    # resources={}
)

