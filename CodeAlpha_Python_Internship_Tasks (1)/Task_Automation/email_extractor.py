"""Extract email addresses from input.txt and save them to emails_found.txt."""
import re
from pathlib import Path

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def main():
    source = Path("input.txt")
    destination = Path("emails_found.txt")

    if not source.exists():
        print("input.txt was not found.")
        print("Create input.txt in this folder and paste the text to scan.")
        return

    text = source.read_text(encoding="utf-8")
    emails = sorted(set(EMAIL_PATTERN.findall(text)), key=str.lower)
    destination.write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Results saved to: {destination.resolve()}")


if __name__ == "__main__":
    main()
