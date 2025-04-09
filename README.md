

 # 📆 GameNite – Auth Setup (Phase 1)
 
 GameNite is a social calendar app designed for coordinating group availability and scheduling events. This stage of the project focuses on user authentication and authorization as a foundational vertical slice.
 
 ## ✅ Features Implemented
 
 - **User Signup & Login**
   - Email + password authentication using Flask + Bcrypt
   - Secure password hashing
 - **Session-Based Auth**
   - Login sets session
   - Logout clears session
   - Session check endpoint (`/check_session`)
 - **Admin Support**
   - `is_admin` flag with protected route for testing admin access
 - **Marshmallow Serialization**
   - Clean, controlled responses from the backend
 - **React Frontend**
   - Fully functional Login and Signup forms using Formik + Yup
   - Routes configured using React Router with protection for `/`
 - **User State**
   - `App.js` tracks logged-in user and redirects based on login status
 - **Modular Routing**
   - Centralized route configuration in `routes.js`
 - **Test Seed Data**
   - Seed script for test users (including an admin)
 
 ## 🧪 Dev Setup
 
 ### Backend
 
 1. Install dependencies:
    ```bash
    pipenv install
    ```
 
 2. Run database migrations:
    ```bash
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    ```
 
 3. Seed the database:
    ```bash
    python server/seed.py
    ```
 
 4. Start the backend server:
    ```bash
    flask run
    ```
 
 ### Frontend
 
 1. From `/client`:
    ```bash
    npm install
    npm start
    ```
 
 ## 🔐 Test Credentials
 
 - **Admin User**
   - Email: `admin@gamenite.dev`
   - Password: `adminpass`
 
 - **Standard Users**
   - Generated via `faker` with password: `password123`
 
 ## 🛠 Next Steps
 
 - Group management (assigning users to groups)
 - Availability submission & display (heatmaps)
 - Threshold-based scheduling logic
 - HubSpot integration and Google Maps visualization