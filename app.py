#!/usr/bin/env python3
import json
import os
import random
from typing import List, Dict, Optional

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "students.json")


def load_students() -> List[Dict[str, str]]:
    if not os.path.exists(DATA_FILE_PATH):
        return []
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                normalized = []
                for item in data:
                    if not isinstance(item, dict):
                        continue
                    name = str(item.get("name", "")).strip()
                    group = str(item.get("group", "")).strip()
                    if name and group:
                        normalized.append({"name": name, "group": group})
                return normalized
            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students: List[Dict[str, str]]) -> None:
    try:
        with open(DATA_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        print(f"Ошибка сохранения: {exc}")


def print_menu() -> None:
    print("\n=== Рандомайзер студентов ===")
    print("1) Добавить студента")
    print("2) Удалить студента")
    print("3) Показать всех студентов")
    print("4) Показать группы и количество")
    print("5) Случайный студент (из всех)")
    print("6) Случайный студент (по группе)")
    print("7) Импорт из JSON")
    print("8) Экспорт в JSON")
    print("0) Выход")


def input_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не может быть пустым. Попробуйте ещё раз.")


def add_student(students: List[Dict[str, str]]) -> None:
    name = input_non_empty("Имя студента: ")
    group = input_non_empty("Номер группы: ")
    students.append({"name": name, "group": group})
    save_students(students)
    print("Добавлено.")


def list_students(students: List[Dict[str, str]]) -> None:
    if not students:
        print("Список пуст.")
        return
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. {s['name']} (группа {s['group']})")


def delete_student(students: List[Dict[str, str]]) -> None:
    if not students:
        print("Список пуст.")
        return
    list_students(students)
    try:
        idx = int(input("Номер для удаления: "))
        if 1 <= idx <= len(students):
            removed = students.pop(idx - 1)
            save_students(students)
            print(f"Удалён: {removed['name']} (группа {removed['group']})")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")


def groups_summary(students: List[Dict[str, str]]) -> Dict[str, int]:
    summary: Dict[str, int] = {}
    for s in students:
        summary[s["group"]] = summary.get(s["group"], 0) + 1
    return summary


def show_groups(students: List[Dict[str, str]]) -> None:
    if not students:
        print("Список пуст.")
        return
    summary = groups_summary(students)
    for group, count in sorted(summary.items(), key=lambda x: x[0]):
        print(f"Группа {group}: {count}")


def random_any(students: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    if not students:
        return None
    return random.choice(students)


def random_by_group(students: List[Dict[str, str]], group: str) -> Optional[Dict[str, str]]:
    filtered = [s for s in students if s["group"].strip() == group.strip()]
    if not filtered:
        return None
    return random.choice(filtered)


def import_json(students: List[Dict[str, str]]) -> None:
    path = input_non_empty("Путь к JSON: ")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Ожидался список объектов.")
            return
        imported: List[Dict[str, str]] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", "")).strip()
            group = str(item.get("group", "")).strip()
            if name and group:
                imported.append({"name": name, "group": group})
        if not imported:
            print("Нет валидных записей для импорта.")
            return
        students.clear()
        students.extend(imported)
        save_students(students)
        print(f"Импортировано записей: {len(imported)}")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Ошибка импорта: {exc}")


def export_json(students: List[Dict[str, str]]) -> None:
    if not students:
        print("Список пуст, экспортировать нечего.")
        return
    path = input_non_empty("Куда сохранить JSON: ")
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        print(f"Сохранено: {path}")
    except OSError as exc:
        print(f"Ошибка экспорта: {exc}")


def main() -> None:
    students: List[Dict[str, str]] = load_students()
    while True:
        print_menu()
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_groups(students)
        elif choice == "5":
            pick = random_any(students)
            if pick:
                print(f"Выбран: {pick['name']} (группа {pick['group']})")
            else:
                print("Список пуст.")
        elif choice == "6":
            group = input_non_empty("Номер группы: ")
            pick = random_by_group(students, group)
            if pick:
                print(f"Выбран: {pick['name']} (группа {pick['group']})")
            else:
                print("В этой группе нет студентов.")
        elif choice == "7":
            import_json(students)
        elif choice == "8":
            export_json(students)
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()

