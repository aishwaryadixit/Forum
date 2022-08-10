"""
The DB model, expressed in Django syntax.

(Keep the class fields alphabetically sorted.)
"""

from django.conf import settings
from django.db.models import (
    CASCADE,
    PROTECT,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
)


class Topic(Model):
    """
    A collection of Questions
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    description = TextField(null=False)
    is_approved = BooleanField(default=False, null=False)
    title = CharField(max_length=40, null=False)


class Question(Model):
    """
    A Question under a Topic.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    description = TextField(null=False)
    is_deleted = BooleanField(default=False, null=False)
    timestamp = DateTimeField(null=False)
    title = CharField(max_length=40, null=False)
    topic = ForeignKey(Topic, on_delete=CASCADE, null=False)


class Response(Model):
    """
    A Response to a Question.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    description = TextField(null=False)
    is_deleted = BooleanField(default=False, null=False)
    question = ForeignKey(Question, on_delete=CASCADE, null=False)
    timestamp = DateTimeField(null=False)


class QuestionUpVotes(Model):
    """
    A user can upvote a Question from another user.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    is_deleted = BooleanField(default=False, null=False)
    question = ForeignKey(Question, on_delete=CASCADE, null=False)
    timestamp = DateTimeField(null=False)


class ResponseUpVotes(Model):
    """
    A user can upvote a Response from another user.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    is_deleted = BooleanField(default=False, null=False)
    response = ForeignKey(Response, on_delete=CASCADE, null=False)
    timestamp = DateTimeField(null=False)


class Tag(Model):
    """
    Multiple users can tag multiple other users in a Question.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    is_deleted = BooleanField(default=False, null=False)
    question = ForeignKey(Question, on_delete=CASCADE, null=False)
    tagged_user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=PROTECT,
        related_name="%(class)s_tagged_user",
    )
    timestamp = DateTimeField(null=False)


class Nomination(Model):
    """
    Multiple users can nominate multiple other users.
    """

    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    is_deleted = BooleanField(default=False, null=False)
    nominated_user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=PROTECT,
        related_name="%(class)s_nominated_user",
    )
    timestamp = DateTimeField(null=False)
