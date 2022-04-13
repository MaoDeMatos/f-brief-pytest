from dataclasses import dataclass


@dataclass
class cat:
  id: int
  name: str

  @classmethod
  def from_dict(cls, data: dict) -> "cat":
    return cls(
      id=data["main"]["id"],
      name=data["main"]["name"],
    )
