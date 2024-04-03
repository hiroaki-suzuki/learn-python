from dataclasses import dataclass
from datetime import datetime


def main() -> None:
    """メイン"""
    in_progress_task = InProgressTask(title="進行中のタスク")
    completed_task = CompletedTask(title="完了したタスク", completed_at=datetime.now())
    # 以下はエラーになる。mypyでもエラーになる。
    # ng_in_progress_task = InProgressTask(title="進行中のタスク", completed_at=datetime.now())

    tasks = [in_progress_task, completed_task]
    for task in tasks:
        match task:
            case InProgressTask(title=title):
                print(f"タイトル：{title}")
            case CompletedTask(title=title, completed_at=completed_at):
                print(f"タイトル：{title}、完了日時：{completed_at}")


@dataclass
class Task:
    title: str


@dataclass
class InProgressTask(Task):
    title: str


@dataclass
class CompletedTask(Task):
    title: str
    completed_at: datetime


if __name__ == "__main__":
    main()
