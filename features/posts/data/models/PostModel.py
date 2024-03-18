from features.posts.domain.entities.Post import Post, PostRead
import logging
from core.utils.MyUtils import MyUtils

appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])


class PostModel(Post):
    """User post model implementation"""

    def update(self, data: dict) -> Post:
        logger = logging.getLogger(appProps["logger"])
        for k, v in data.items():
            logger.info(
                f"updating value of '{k}' from '{getattr(self, k, None)}' to '{v}'"
            )
            setattr(self, k, v)
        return self


class PostReadModel(PostRead):
    pass
