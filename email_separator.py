import re
import pandas as pd
import questionary
from pathlib import Path


__author__ = "Ritesh Karmakar"
__license__ = "MIT"
__version__ = "1.0.0"
__github__ = "https://github.com/riteshkarmakar/email-separator"

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def is_valid_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email)   


def show_copyright():
    print(
        " ================================================================",
        f" Email Sender - Version {__version__}",
        f" Copyright (c) {__author__}",
        f" License: {__license__}",
        f" GitHub: {__github__}",
        " ================================================================",
        sep="\n"
    )


def separate_emails(file_path: Path, email_column_name: str):
    df = pd.read_excel(file_path)
    result_df = pd.DataFrame(columns=df.columns)
    
    for _, row in df.iterrows():
        emails = [email.strip() for email in re.split(r"[,/;]", str(row[email_column_name]))]
        
        # Create a new row for each email
        for email in emails:
            if not is_valid_email(email):
                email = questionary.text(
                    f"{email} is not a valid email. Please enter a valid email:",
                    validate=lambda email: True if is_valid_email(email) else "Invalid Email",
                    qmark=""
                ).ask()

            new_row = row.copy()
            new_row[email_column_name] = email
            result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
    
    new_path = file_path.with_stem(file_path.stem + "_modified")
    result_df.to_excel(new_path, index=False)
    questionary.print(f" Emails separated and saved to {new_path.as_posix()!r}", style="fg:green")


if __name__ == "__main__":
    show_copyright()

    file_path = questionary.path(
        "Enter the path of the Excel file:",
        validate=lambda path: True if path.endswith(".xlsx") else "Only Excel file (.xlsx) is allowed",
        qmark=""
    ).ask()

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        questionary.print(f" Error reading file: {e}", style="fg:red")
    else:
        email_column_name = questionary.select("Select the Email Column Name:", choices=list(df), qmark="").ask()
        separate_emails(Path(file_path), email_column_name)

    questionary.press_any_key_to_continue("Press any key to Exit...").ask()
