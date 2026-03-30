import json
import os
from datetime import datetime

FILE_NAME = "todo.json"
# feature ui title

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(tasks):
    title = input("할 일 입력: ")
    task = {
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    print("추가 완료")


def show_tasks(tasks):
    if not tasks:
        print("할 일이 없습니다.")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']} ({task['created_at']})")


def complete_task(tasks):
    show_tasks(tasks)
    idx = int(input("완료할 번호: "))
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        print("완료 처리됨")


def delete_task(tasks):
    show_tasks(tasks)
    idx = int(input("삭제할 번호: "))
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        print("삭제 완료")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. 추가  2. 목록  3. 완료  4. 삭제  5. 종료")
        choice = input("선택: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("저장 후 종료")
            break
        else:
            print("잘못된 입력")


if __name__ == "__main__":
    main()