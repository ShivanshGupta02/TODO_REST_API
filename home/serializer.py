from rest_framework import serializers
from .models import Todo
import re 
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields = ["user","todo_title","slug","todo_description","uid"]
        # excludes = ['created_at']
        
    
    def get_slug(self,obj):
        return slugify(obj.todo_title)
        
    # def validate(self,validated_data):
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError("TODO title can't contain specical character")
    #     return validated_data
    
    # ========= for specific validation on a perticular field ==========
    
    def validate_todo_title(self,data):
        if data:
            todo_title = data 
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(todo_title) <= 3:
                raise serializers.ValidationError('Todo title must be more than 3 chars')
            
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError("TODO title can't contain specical character")
        return data
    
    
from .models import TimingTodo    
    
class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        
        # Caution !! - It serializes all the fields related to foreign key
        # depth=1
        


                