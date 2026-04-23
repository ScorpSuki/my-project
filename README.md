# My Project - Student App

Бұл CI/CD pipeline бар демонстрациялық Python қосымшасы.

## Құрылым:
- `.github/workflows/ci.yml` - GitHub Actions CI/CD конфигурациясы
- `app.py` - Негізгі қосымша коды
- `tests/` - Тест файлдары
- `Dockerfile` - Docker контейнерін құруға арналған файл

## CI/CD Pipeline не істейді:
1. Python 3.10 орнатады
2. Тәуелділіктерді орнатады
3. Тестерді жүгізеді
4. Docker image құрады
5. Контейнерді іске қосады
