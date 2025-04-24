from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# gsheets URL
sheet_id = "14TPNWMPCNZi4DIhqUTOFJYHZShPuuQfodWDhE2-0I8Y"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# gsheets URL
sheet_id = "14TPNWMPCNZi4DIhqUTOFJYHZShPuuQfodWDhE2-0I8Y"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

@app.route('/')
def index():
    df = pd.read_csv(sheet_url)
    search_query = request.args.get('query', '')
    search_field = request.args.get('field', 'All')

    if search_query:
        if search_field == 'All':
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        else:
            df = df[df[search_field].astype(str).str.contains(search_query, case=False)]

    df = df.dropna(subset=['Title'])
    df = df.sort_values(by='Title', key=lambda col: col.str.lower())

    books = df.to_dict(orient='records')
    return render_template('index.html', books=books, query=search_query, field=search_field)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)