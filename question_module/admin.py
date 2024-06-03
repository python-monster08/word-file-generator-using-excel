from django.contrib import admin
from .models import Question, DefficultyLevel
from django.utils.html import mark_safe, escape

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_no', 'display_question_text', 'year', 'correct_answer_option', 'marks', 'negative_marks')
    list_filter = ('year', 'question_type')
    search_fields = ('question_text', 'list_i_heading', 'list_ii_heading')
    fieldsets = (
        ('Basic Information', {
            'fields': ('question_no', 'question_text', 'year', 'assertion', 'reason','image','list_i_selection_text')
        }),
        ('Table Data', {
            'fields': ('table_head_a', 'table_head_b', 'table_head_c', 'table_head_d',
                        'head_a_data1','head_a_data2','head_a_data3','head_a_data4',
                        'head_b_data1','head_b_data2','head_b_data3','head_b_data4',
                        'head_c_data1','head_c_data2','head_c_data3','head_c_data4',
                        'head_d_data1','head_d_data2','head_d_data3','head_d_data4',
                        )
        }),
        ('Options', {
            'fields': ('list_i_option_a', 'list_i_option_b', 'list_i_option_c', 'list_i_option_d',
                       'list_ii_option_1', 'list_ii_option_2', 'list_ii_option_3', 'list_ii_option_4', 'list_ii_option_5',
                       'option_a', 'option_b', 'option_c', 'option_d', 'option_e')
        }),
        ('Answer Details', {
            'fields': ('correct_answer_option', 'correct_answer_description', 'question_type', 'marks', 'negative_marks')
        }),
        ('Extra Details', {
            'fields': ('area', 'topic', 'level_of_defficulty')
        }),
    )
    def display_question_text(self, obj):
        return mark_safe(obj.question_text)
# Register the admin class with the associated model
admin.site.register(Question, QuestionAdmin)


admin.site.register(DefficultyLevel)