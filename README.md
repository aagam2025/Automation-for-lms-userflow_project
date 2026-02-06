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
  base_page.py        # Base page class for common actions
  login_page.py       # Login page actions
  add_course_page.py  # Add course actions
  add_user.py         # Add user actions
  course_page.py      # Course management actions
  course_assign_page.py # Course assignment actions
tests/
  test_login.py       # Login tests
  test_addcourse.py   # Add course tests
  test_adduser.py     # Add user tests
  test_course.py      # Course search tests
  test_courseassign.py# Course assignment tests
```

## Getting Started

### Prerequisites
- Python 3.7+
- Node.js (for Playwright browser installation)

### Installation
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd Automation_of_Lms_User_flow
   ```
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```sh
   playwright install
   ```

### Running Tests
Run all tests with:
```sh
pytest
```

## Configuration
- Update credentials and URLs in `config/config.py` as needed.
- Device emulation and timeouts are also configurable in `config/config.py`.

## Notes
- All test data (emails, course names, etc.) are for demo purposes.
- No real user data is included.

## License
MIT License
