from pydantic import EmailStr
from datetime import datetime
from typing import Optional


class Runner:
    def __init__(
      self,
      id: int,
      name: str,
      email: EmailStr,
      password: str,
      image: str,
      status: str,
      deleted_at: Optional[datetime],
    ):
      self.id = id
      self.name = name
      self.email = email
      self.password = password
      self.image = image
      self.status = status
      self.deleted_at = deleted_at

    def get_name(self):
      return self._name

    def set_name(self, name: str) -> None:
      if not isinstance(name, str):
          raise TypeError("O nome deve ser uma string")
      if len(name) > 50:
          raise ValueError("O nome deve ter no máximo 50 caracteres")

      self._name = name
