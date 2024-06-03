# web-proto-boots5
Web Prototyping using Flask, jinja2, Bootstrap 5 (bundle version), and FontAwesome. Very simple and straightforward idea here. Just serving Flask app, using development server, but, remember:  Do not use it in a production deployment. Use a production WSGI server instead.

The ideia here is: the Flask application displays a simple home page at the root URL (`/`) and a dashboard with dummy metrics at the `/home` URL, accessible only to logged-in users.

### Updated Project Structure

```plaintext
my_flask_project/
├── .gitignore
├── requirements.txt
├── app.py
└── static/
    ├── img/
        └── logo.png
        └── favicon.ico
└── templates/
    ├── base.html
    ├── index.html
    ├── home.html
    ├── topbar.html
    └── footer.html
```


### Running the Project

1. Ensure you are in the project directory and your virtual environment is activated.
2. Install the dependencies if you haven't already:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Flask application:
    ```sh
    python app.py
    ```
4. Open your browser and navigate to `http://127.0.0.1:8888/` for the root page and `http://127.0.0.1:8888/home` for the dashboard (simulated authentication).

### Testing Authentication

- To simulate logging in, navigate to `http://127.0.0.1:8888/login`.
- To simulate logging out, navigate to `http://127.0.0.1:8888/logout`.

