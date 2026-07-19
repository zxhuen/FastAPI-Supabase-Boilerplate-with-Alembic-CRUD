## Setup

### 1. Clone the repository

```bash
git clone https://github.com/zxhuen/FastAPI-Supabase-Boilerplate-with-Alembic-CRUD.git
```

Navigate to the project directory:

```bash
cd <your-repository>
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your `.env`

Create a `.env` file in the project root and add the following:

```env
DATABASE_URL=
SUPABASE_URL=
SUPABASE_KEY=
```

- **`DATABASE_URL`**
  - Supabase Dashboard → **Connect** → **ORM**
  - Copy the **Pooler** connection string.
  - Remove `?pgbouncer=true` if your project requires it.

- **`SUPABASE_URL`**
  - Supabase Dashboard → **Project URL**

- **`SUPABASE_KEY`**
  - Supabase Dashboard → **Project Settings** → **API Keys**
  - Copy the `anon` or `service_role` key depending on your use case.

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Open the Swagger UI:

```
http://127.0.0.1:8000/docs
```

### will add pytest and logs soon
