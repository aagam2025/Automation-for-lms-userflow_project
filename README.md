# Automation of LMS User Flow

This project automates user flows for an LMS (Learning Management System) using Python, Playwright, and Pytest.

## Features
- Automated login, course management, user management, and course assignment flows
- Page Object Model structure for maintainable and scalable tests
- Device emulation and configurable timeouts
- Easy test execution with Pytest

## Project Structure
```
conftest.py           # Pytest fixtures and Playwright setup
pytest.ini            # Pytest configuration
requirements.txt      # Python dependencies
config/
  config.py           # Project configuration (URLs, credentials, device settings)
pages/
  login_page.py       # Login page actions
  add_course_page.py  # Add course actions
  add_user.py         # Add user actions
  course_page.py      # Course management actions
  course_assign_page.py # Course assignment actions
  course_start.py     # Course start actions
tests/
  test_login.py       # Login tests
  test_addcourse.py   # Add course tests
  test_adduser.py     # Add user tests
  test_course_search.py # Course search tests
  test_courseassign.py# Course assignment tests
  test_course_start.py # Course start tests
```

## Getting Started

### Prerequisites
- Python 3.7+

### Installation
1. Clone the repository:
   
```
sh
   git clone <your-repo-url>
   cd Automation_of_Lms_User_flow
   
```
2. Create and activate a virtual environment:
   
```
sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
```
3. Install Python dependencies:
   
```
sh
   pip install -r requirements.txt
   
```
4. Install Playwright browsers:
   
```
sh
   playwright install
   
```

### Running Tests
Run all tests with:
```
sh
   pytest
```

## Configuration
- Update credentials and URLs in `config/config.py` as needed.
- Device emulation and timeouts are also configurable in `config/config.py`.

## Notes
- All test data (emails, course names, etc.) are for demo purposes.
- No real user data is included.
