from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

# Register your models here.

admin.site.site_header = 'Моя адмінка'


class RatingFilter(admin.SimpleListFilter):
    title = 'Фільтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низький'),
            ('від 40 до 59', 'Середній'),
            ('від 60 до 79', 'Високий'),
            ('>=80', 'Найвищий'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'від 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'від 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'director', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'director', 'currency', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollar', 'set_euro']
    filter_horizontal = ['actors']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(ordering='rating', description='Personal Opinion')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Навіщо це дивитися'
        if mov.rating < 70:
            return 'Разок можна глянути'
        if mov.rating <= 85:
            return 'Непоганий фільм'
        return 'Топчик'

    @admin.action(description='Зміна курсу валют на Долар')
    def set_dollar(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.USD)
        self.message_user(request, f'Було виконано {count_update} операцій')

    @admin.action(description='Зміна курсу валют на Євро')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Було виконано {count_update} операцій', messages.ERROR)


admin.site.register(Director)
admin.site.register(Actor)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']
