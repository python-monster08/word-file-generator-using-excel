from django.db import models
from django.utils.html import mark_safe

# Create Difficulty level Model
class DefficultyLevel(models.Model):
    level = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.level
   

# Create Question Model 
class Question(models.Model):
    question_no = models.IntegerField(default='')
    question_text = models.TextField(default='')
    year = models.CharField(max_length=10,null=True, blank=True, default='')
    assertion = models.TextField(null=True, blank=True, default='')
    reason = models.TextField(null=True, blank=True, default='')
    list_i_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_a = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_b = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_c = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_d = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_e = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_f = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_g = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_option_h = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_option_1 = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_option_2 = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_option_3 = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_option_4 = models.CharField(max_length=100, null=True, blank=True, default='')
    list_ii_option_5 = models.CharField(max_length=100, null=True, blank=True, default='')
    option_a = models.CharField(max_length=100, null=True, blank=True, default='')
    option_b = models.CharField(max_length=100, null=True, blank=True, default='')
    option_c = models.CharField(max_length=100, null=True, blank=True, default='')
    option_d = models.CharField(max_length=100, null=True, blank=True, default='')
    option_e = models.CharField(max_length=100, null=True, blank=True, default='')
    list_i_selection_text = models.TextField(null=True, blank=True, default='')
    correct_answer_option = models.CharField(max_length=1, default='')
    correct_answer_description = models.TextField(null=True, blank=True, default='')
    question_type = models.CharField(max_length=50, default='multiple_choice')
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=4)
    negative_marks = models.DecimalField(max_digits=5, decimal_places=2, default=1.33)
    image = models.ImageField(upload_to="questions_images", null = True, blank = True)

    # New fields based on the table headings in the image
    table_head_a = models.CharField(max_length=100, null=True, blank=True)
    table_head_b = models.CharField(max_length=100, null=True, blank=True)
    table_head_c = models.CharField(max_length=100, null=True, blank=True)
    table_head_d = models.CharField(max_length=100, null=True, blank=True)
    head_a_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data4 = models.CharField(max_length=100, null=True, blank=True)

    # extra details for filtration
    area = models.CharField(max_length=100, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    level_of_defficulty = models.ForeignKey(DefficultyLevel, on_delete=models.CASCADE, null=True, default=2)


    def __str__(self):
        return mark_safe(self.question_text)
    
    def get_options(self):
        # Return only non-empty options
        options = [self.option_a, self.option_b, self.option_c, self.option_d, self.option_e]
        return [opt for opt in options if opt]  # This filters out None or empty string options

    def get_list_i_options(self):
        options = [
            self.list_i_option_a, 
            self.list_i_option_b, 
            self.list_i_option_c, 
            self.list_i_option_d
        ]
        return [opt for opt in options if opt]  # Only return non-empty options