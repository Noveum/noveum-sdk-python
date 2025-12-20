from enum import Enum


class PostApiAiChatsResponse200MessagesItemRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
