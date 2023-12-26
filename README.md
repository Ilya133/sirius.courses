**1. Установить необходимые зависимости из requirements.txt**

**2. Запуск тестов можно выполнить следующими командами:**
> В директории:
>  ```sh
> ~/PycharmProjects/test_task_sirius/tests$
> ```
> Если запускать тесты в один поток: 
>  ```sh
>  pytest register_page.py
>  ```

> Если параллельно в 2 воркера: 
>  ```sh
>  pytest register_page.py -n=2 --dist loadgroup
>  ```
