from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        help_text=_(
            "Required. 32 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    first_name = None
    last_name = None

    def get_full_name(self):
        return self.__str__()

    def get_short_name(self):
        return self.__str__()

    @property
    def display_name(self):
        return self.profile.display_name

    @property
    def pronouns(self):
        return self.profile.pronouns

    def __str__(self):
        if self.profile.display_name:
            return self.profile.display_name
        return self.username


class Profile(models.Model):
    PRONOUN_CHOICES = (
        ('M', _('he/him')),
        ('F', _('she/her')),
        ('N', _('they/them')),
    )

    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    display_name = models.CharField(
        _('display name'),
        max_length=32,
        blank=True,
        help_text=_('Your display name, this is shown instead of your username.'),
    )
    pronouns = models.CharField(
        _('pronouns'),
        max_length=1,
        blank=True,
        choices=PRONOUN_CHOICES,
        help_text=_('Your preferred pronouns, these are sometimes displayed alongside your name.'),
    )

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return self.user.username