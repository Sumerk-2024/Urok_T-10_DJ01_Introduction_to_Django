from django.http import HttpResponse


def home_view(request):
    return HttpResponse("""
        <h1>Добро пожаловать на главную страницу</h1>
        <p>Это главная страница нашего сайта. Перейдите по ссылкам, чтобы увидеть другие страницы.</p>
        <ul>
            <li><a href="/data/">Страница данных</a></li><br>
            <li><a href="/test/">Тестовая страница</a></li>
        </ul>
    """)


def data_view(request):
    return HttpResponse("""
        <h1>Страница данных</h1>
        <p>Здесь находятся данные нашего приложения. Подробная информация о данных будет отображаться здесь.</p>
        <ul>
            <li><a href="/">Главная страница</a></li><br>
            <li><a href="/test/">Тестовая страница</a></li>
        </ul>
    """)


def test_view(request):
    return HttpResponse("""
        <h1>Тестовая страница</h1>
        <p>Это тестовая страница для проверки работы нашего приложения. Здесь можно увидеть примеры тестов и их результаты.</p>
        <ul>
            <li><a href="/">Главная страница</a></li><br>
            <li><a href="/data/">Страница данных</a></li>
        </ul>
    """)
