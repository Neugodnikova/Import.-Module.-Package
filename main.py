from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from colorama import Fore, Style

if __name__ == '__main__':
    print(f"Текущая дата: {datetime.now().date()}")
    calculate_salary()
    get_employees()
    print(Fore.GREEN + "Этот текст будет зеленым" + Style.RESET_ALL)
