from typing import *


class MultiIndex:
    @classmethod
    def from_product(iterables=...):
        "usage.xarray: 39"

    @classmethod
    def from_arrays(
        arrays: list,
        names: Union[
            (
                List[Literal[("x", "y")]],
                Tuple[(Literal[("level_str",)], Literal[("level_date",)])],
                pandas.core.indexes.frozen.FrozenList,
                List[Literal[("y2", "x", "y1", "y")]],
            )
        ],
    ):
        "usage.xarray: 8"

    @classmethod
    def from_tuples(
        tuples: Union[
            (
                Tuple[
                    (
                        Tuple[(Literal[("a",)], int)],
                        Tuple[(Literal[("a",)], int)],
                        Tuple[(Literal[("b",)], int)],
                        Tuple[(Literal[("b",)], int)],
                    )
                ],
                List[List[int]],
                Tuple[
                    (
                        Tuple[(Literal[("b",)], int)],
                        Tuple[(Literal[("b",)], int)],
                        Tuple[(Literal[("a",)], int)],
                        Tuple[(Literal[("a",)], int)],
                    )
                ],
            )
        ],
        names: List[Literal[("level0", "two", "level1", "one")]],
    ):
        "usage.xarray: 3"

    dtype = ...
    values = ...
    names = ...
    name = ...
    nlevels = ...
    levels = ...
    codes = ...
    is_unique = ...
    shape = ...
    rename = ...
    size = ...
    is_monotonic = ...

    def __getitem__(self, _0, /):
        ""

    def append(self, /, other: List[pandas.core.indexes.multi.MultiIndex]):
        "usage.xarray: 3"

    def equals(self, /, other: pandas.core.indexes.multi.MultiIndex):
        "usage.xarray: 8"

    def get_level_values(
        self,
        /,
        level: Literal[
            (
                "level_2",
                "level_str",
                "dim2",
                "dim1",
                "y",
                "level_date",
                "x",
                "one",
                "variable",
                "a_quite_long_level_name",
                "two",
                "level_1",
            )
        ],
    ):
        "usage.xarray: 27"

    def get_loc(self, /, key: Tuple[(Literal[("b", "a")], int, int)]):
        "usage.xarray: 3"

    def get_loc_level(self, /, key, level):
        "usage.xarray: 12"

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 2"

    def remove_unused_levels(self, /):
        "usage.xarray: 1"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def reorder_levels(self, /, order: List[Literal[("level_2", "level_1")]]):
        "usage.xarray: 4"

    def set_names(self, /, names: List[Literal[("level0", "level1")]]):
        "usage.xarray: 1"

    def set_levels(
        self,
        /,
        levels: List[
            Union[
                (pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index)
            ]
        ],
    ):
        "usage.xarray: 1"

    def _get_level_number(self, /, level: int):
        "usage.xarray: 1"

    def get_locs(
        self, /, seq: Tuple[(slice[(None, None, None)], int, Literal[("no_level",)])]
    ):
        "usage.xarray: 1"