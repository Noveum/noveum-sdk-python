from enum import Enum


class GetApiAiChatsResponse200ItemMessagesItemRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
