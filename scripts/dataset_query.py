#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
LLM Test Dataset Query Tool
Extract questions, answers, and statistics from the dataset
"""

import json
import os
import sys
import argparse
from typing import Optional

# Fix Windows console encoding issues
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class DatasetQuery:
    """Dataset query tool"""

    ZH_JSON = "dataset.zh.json"
    EN_JSON = "dataset.json"

    def __init__(self, lang: Optional[str] = None):
        self.dataset = None
        self.dataset_path = None
        self.lang = lang or self._auto_detect_lang()
        self._load_dataset()

    def _auto_detect_lang(self) -> str:
        """Auto-detect language based on user input"""
        # Check command-line arguments
        for arg in sys.argv[1:]:
            if any("\u4e00" <= c <= "\u9fff" for c in arg):
                return "zh"

        # Check environment variables
        lang = os.environ.get("LANG", "") or os.environ.get("LC_ALL", "")
        if "zh" in lang.lower():
            return "zh"

        # Check console encoding
        console_encoding = sys.stdout.encoding or ""
        if console_encoding and any(
            "\u4e00" <= c <= "\u9fff" for c in console_encoding
        ):
            return "zh"

        return "en"

    def _load_dataset(self):
        """Load dataset"""
        filename = self.ZH_JSON if self.lang == "zh" else self.EN_JSON

        # Try multiple paths
        possible_paths = [
            filename,
            os.path.join(os.path.dirname(__file__), filename),
            os.path.join(os.path.dirname(__file__), "..", filename),
            os.path.join(os.path.dirname(__file__), "..", "resources", filename),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                self.dataset_path = path
                break
        else:
            raise FileNotFoundError(f"Dataset file not found: {filename}")

        with open(self.dataset_path, "r", encoding="utf-8") as f:
            self.dataset = json.load(f)

    def total(self) -> int:
        """Get total number of questions"""
        return len(self.dataset)

    def question(self, index: int) -> Optional[str]:
        """Get question by index"""
        for item in self.dataset:
            if item["index"] == index:
                return item["question"]
        return None

    def answer(self, index: int) -> Optional[str]:
        """Get answer by index"""
        for item in self.dataset:
            if item["index"] == index:
                return item["human_answer"]
        return None

    def category(self, index: int) -> Optional[str]:
        """Get category by index"""
        for item in self.dataset:
            if item["index"] == index:
                return item["category"]
        return None

    def get_item(self, index: int) -> Optional[dict]:
        """Get full item by index"""
        for item in self.dataset:
            if item["index"] == index:
                return item
        return None

    def all_categories(self) -> list:
        """Get all categories"""
        return sorted(set(item["category"] for item in self.dataset))


def print_usage():
    """Print usage"""
    print("=" * 60)
    print("LLM Test Dataset Query Tool")
    print("=" * 60)
    print()
    print("Usage:")
    print("  python dataset_query.py total               - Total number of questions")
    print("  python dataset_query.py question <index>   - Get question by index")
    print("  python dataset_query.py answer <index>     - Get answer by index")
    print("  python dataset_query.py categories          - List all categories")
    print()
    print("Language options:")
    print("  -l, --lang <zh|en>  - Specify dataset language (default: auto)")
    print()
    print("Examples:")
    print("  python dataset_query.py total")
    print("  python dataset_query.py question 1")
    print("  python dataset_query.py answer 31")
    print("  python dataset_query.py question 1 -l zh")
    print("  python dataset_query.py answer 31 --lang en")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="LLM Test Dataset Query Tool")
    parser.add_argument("-l", "--lang", choices=["zh", "en"], help="Dataset language")
    parser.add_argument(
        "command", nargs="?", help="Command: total, question, answer, categories"
    )
    parser.add_argument("index", nargs="?", type=int, help="Question index")

    args = parser.parse_args()

    if args.command is None:
        print_usage()
        sys.exit(0)

    try:
        query = DatasetQuery(lang=args.lang)

        cmd = args.command.lower()

        if cmd == "total":
            print(f"Total: {query.total()}")

        elif cmd == "question" and args.index is not None:
            question = query.question(args.index)
            if question:
                print(question)
            else:
                print(f"Question #{args.index} not found")

        elif cmd == "answer" and args.index is not None:
            answer = query.answer(args.index)
            if answer:
                print(answer)
            else:
                print(f"Answer #{args.index} not found")

        elif cmd == "categories":
            print("Categories:")
            for cat in query.all_categories():
                print(f"  - {cat}")

        else:
            print_usage()
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
