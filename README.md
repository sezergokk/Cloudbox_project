CloudBox API

CloudBox is a simple FastAPI-based backend service that allows users to upload files which are then stored in Supabase Storage. The API returns a public URL to access the uploaded files.

Features

- Upload files via `/upload` endpoint
- Files are securely stored in Supabase Storage
- Public URLs returned for easy access
- Simple and minimalistic FastAPI backend

Getting Started

Prerequisites

- Python 3.9+
- Supabase account and project
- Git

Setup

1. Clone the repository:

git clone https://github.com/yourusername/cloudbox_project.git
# then go to the project folder 

2. Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows PowerShell

3. Install dependencies:

pip install -r requirement.txt

4. Setup your .env file in the project root with these variables:

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-api-key
SUPABASE_BUCKET=uploads

5. Run the application:

python -m uvicorn app.main:app --reload

6. Open your browser and go to:

http://127.0.0.1:8000/docs

Use the Swagger UI to test the /upload endpoint.

USAGE

Use the /upload POST endpoint to upload files.

The response contains the filename and the public URL of the uploaded file.

License
MIT License