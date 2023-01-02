from django.contrib import admin
from .models import Question, Answer
# Register your models here.

# DB 검색 
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# DB 에 모델 등록
admin.site.register(Question, QuestionAdmin)