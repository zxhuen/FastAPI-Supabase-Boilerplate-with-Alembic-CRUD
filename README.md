## Setup

### 1. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your `.env`

```env
DATABASE_URL=
SUPABASE_URL=
SUPABASE_KEY=
```

- `DATABASE_URL`
  - Supabase Dashboard → Connect → ORM
  - Copy the **Pooler** connection string.
  - Remove `?pgbouncer=true` if your project requires it.

- `SUPABASE_URL`
  - Supabase Dashboard → Project URL

- `SUPABASE_KEY`
  - Project Settings → API Keys → Legacy `anon` or `service_role`

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```
