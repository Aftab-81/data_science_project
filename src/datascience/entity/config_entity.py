from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str
    local_data_file: Path
    store_dir: Path 


from dataclasses import dataclass 
from pathlib import Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    store_data_dir: Path
    STATUS_FILE: str
    all_schema: dict