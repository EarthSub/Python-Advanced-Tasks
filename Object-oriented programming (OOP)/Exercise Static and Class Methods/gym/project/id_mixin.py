

class IDMixin:
    id: int = 1

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id

    @classmethod
    def increment_id(cls) -> None:
        cls.id += 1
