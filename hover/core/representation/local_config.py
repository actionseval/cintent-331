import hover
from hover.config_constants import (
    ConfigSection as Section,
    ConfigKey as Key,
)

KWARG_TRANSLATOR = {
    "dimension": {
        "umap": "n_components",
        "ivis": "embedding_dims",
    },
}

DEFAULT_REDUCTION_METHOD = hover.config[Section.DATA_EMBEDDING][
    Key.DEFAULT_REDUCTION_METHOD
]
