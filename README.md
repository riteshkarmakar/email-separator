# Email Separator

A simple Python script to separate multiple email addresses stored in a single cell of an Excel file.

## Features
✅ Extracts multiple emails from a single cell.  
✅ Validates email addresses.  
✅ Allows user correction for invalid emails.  
✅ Saves a new modified Excel file.  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/riteshkarmakar/email-separator.git
cd email_separator
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the script and follow the prompts:
```
python email_separator.py
```

## Example

### Input Excel File:
| Name      | Emails                                |
|-----------|---------------------------------------|
| John Doe  | john@example.com, jane@example.com    |
| Alice     | alice@example.com / smith@example.com |
| Ram     | ram@example.com ;sharma@example.com     |

### Output Excel File:
| Name      | Emails                                |
|-----------|---------------------------------------|
| John Doe  | john@example.com                      |
| John Doe  | jane@example.com                      |
| Alice     | alice@example.com                     |
| Alice     | smith@example.com                     |
| Ram       | ram@example.com                       |
| Ram       | sharma@example.com                    |


## License
This project is licensed under the **MIT License**.

## Credits
- Developed by [Ritesh Karmakar](https://github.com/riteshkarmakar)
- Inspired by real-world data cleaning challenges.