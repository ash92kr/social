from django.views.generic import TemplateView

class HomePage(TemplateView):  # 홈페이지 클래스의 이름은 template의 기능을 받아 view를 출력함 -> 값으로 index.html 출력
    template_name = 'index.html'  # CBV(class based view)
    
class ByePage(TemplateView):
    template_name = 'bye.html'