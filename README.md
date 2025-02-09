
## Prerequisites

- **Python 3.10+**
- **pip** or **pipenv**


## Installation

**Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
**Create a virtual environment**:
   ```bash
   python3.10 -m venv .venv
   ```
**Activate the virtual environment**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```
**Upgrade Pip**:
   ```bash
   python -m pip install --upgrade pip
   ```
**Add Gitignore**:

   ```bash
   echo "*" > .venv/.gitignore
   ```

**Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
 .venv/bin/uvicorn main:app --reload
```

Open a web browser and go to `http://localhost:8000/docs`.