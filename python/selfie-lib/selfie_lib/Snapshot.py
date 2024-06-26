from typing import Union, Iterable, Dict
from .SnapshotValue import SnapshotValue, SnapshotValueBinary, SnapshotValueString
from .ArrayMap import ArrayMap


class Snapshot:
    def __init__(
        self,
        subject: SnapshotValue,
        facet_data: ArrayMap[str, SnapshotValue] = ArrayMap.empty(),
    ):
        self._subject = subject
        self._facet_data = facet_data

    @property
    def subject(self) -> SnapshotValue:
        return self._subject

    @property
    def facets(self) -> ArrayMap[str, SnapshotValue]:
        return self._facet_data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Snapshot):
            return NotImplemented
        return self._subject == other._subject and self._facet_data == other._facet_data

    def __hash__(self) -> int:
        return hash((self._subject, tuple(self._facet_data.items())))

    def plus_facet(
        self, key: str, value: Union[bytes, str, SnapshotValue]
    ) -> "Snapshot":
        if key == "":
            raise ValueError("The empty string is reserved for the subject.")
        new_facet_data = self._facet_data.plus(key, SnapshotValue.of(value))
        return Snapshot(self._subject, new_facet_data)

    def subject_or_facet_maybe(self, key: str) -> Union[SnapshotValue, None]:
        return self._subject if key == "" else self._facet_data.get(key)

    def subject_or_facet(self, key: str) -> SnapshotValue:
        value = self.subject_or_facet_maybe(key)
        if value is None:
            raise KeyError(f"'{key}' not found in snapshot.")
        return value

    @staticmethod
    def of(data: Union[bytes, str, SnapshotValue]) -> "Snapshot":
        if not isinstance(data, SnapshotValue):
            data = SnapshotValue.of(data)
        return Snapshot(data, ArrayMap.empty())

    @staticmethod
    def of_entries(entries: Iterable[Dict[str, SnapshotValue]]) -> "Snapshot":
        root = None
        facets = ArrayMap.empty()
        for entry in entries:
            key, value = entry["key"], entry["value"]
            if key == "":
                if root is not None:
                    raise ValueError("Duplicate root snapshot detected")
                root = value
            else:
                facets = facets.plus(key, value)
        return Snapshot(root if root else SnapshotValue.of(""), facets)

    @staticmethod
    def _unix_newlines(string: str) -> str:
        return string.replace("\\r\\n", "\\n")
