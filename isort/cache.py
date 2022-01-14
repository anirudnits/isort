import pickle
from typing import Dict, Iterator, Tuple

from _version import __version__
from pathlib import Path
from platformdirs import user_cache_dir

from settings import Config


# types
Timestamp = float
FileSize = int
CacheInfo = Tuple[Timestamp, FileSize]
Cache = Dict[str, CacheInfo]

CACHE_DIR = Path(user_cache_dir("isort", version=__version__))

def read_cache(config: Config) -> Cache:
    """
    Reads the cache file from disk specific to the configuration and version and returns the latest cache information.

    If the file doesn't exist or is ill-formatted, returns an empty Cache object instead.
    """
    cache_file = CACHE_DIR / "isort-cache"
    if not cache_file.exists():
        return {}
    with cache_file.open("rb") as f:
        return pickle.load(f)


def get_config_hash(config: Config) -> str:
    """
    Returns a hash of the configuration.
    """
    return hash(frozenset(config.__dict__.items()))


def get_cached_config(config: Config) -> Dict:
    pass


def get_cache_info(cache: Cache, file: Path) -> CacheInfo:
    pass


def is_formatted(cache: Cache, file: Path) -> bool:
    pass


def write_cache(config: Config, files: Iterator[Path]) -> None:
    pass
