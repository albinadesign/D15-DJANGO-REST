from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Category, PostCategory
from django.utils.translation import pgettext_lazy

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
    added_after=DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type':'date'},
        ),
        label=pgettext_lazy('date of creation', 'Posted after')
    )

    category = ModelMultipleChoiceFilter(
        field_name = 'postCategory',
        queryset=Category.objects.all(),
        label=pgettext_lazy('Category name', 'Category name'),
        conjoined=False,
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
        }