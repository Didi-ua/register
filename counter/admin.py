from django.contrib import admin, messages

from .models import Counter, History


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'current_value')
    exclude = ('id',)

    def save_model(self, request, obj, form, change):
        if change:
            actual_obj = Counter.objects.get(id=obj.id)
            if obj.current_value < actual_obj.current_value:
                obj.current_value = actual_obj.current_value
                messages.error(request, 'value cannot decrease')
            elif obj.current_value != actual_obj.current_value:
                History.objects.create(
                    type=History.UserType.OPERATOR,
                    value=obj.current_value,
                    consumption=obj.current_value - actual_obj.current_value,
                    counter=obj
                )
        super().save_model(request, obj, form, change)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('period', 'type', 'value', 'consumption', 'counter')
    exclude = ('id',)
    readonly_fields = ('type',)

