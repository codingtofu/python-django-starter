from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'image': _('이미지의 url을 입력해주세요'),
            'password': _('게시물 비밀번호를 입력해주세요.'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'name': {
                'max_length': _('이름이 너무 깁니다. 30자 이하로 해주세요.')
            },
            'image': {
                'max_length': _('이미지 주소의 길이가 너무 깁니다. 500자 이하로 해주세요.')
            },
            'password': {
                'max_length': _('비밀번호가 너무 깁니다. 20자 이하로 해주세요.')
            }
        }


class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']