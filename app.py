from flask import Flask, render_template, request, abort
import pandas as pd

app = Flask(__name__)

# Google Sheets URL
sheet_id = "14TPNWMPCNZi4DIhqUTOFJYHZShPuuQfodWDhE2-0I8Y"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

def get_books_data():
    """Fetch and return books data from Google Sheets"""
    try:
        df = pd.read_csv(sheet_url)
        df = df.dropna(subset=['Title'])
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

@app.route('/')
def index():
    """Main library page with search functionality"""
    df = get_books_data()
    search_query = request.args.get('query', '')
    search_field = request.args.get('field', 'All')

    if search_query and not df.empty:
        if search_field == 'All':
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        else:
            if search_field in df.columns:
                df = df[df[search_field].astype(str).str.contains(search_query, case=False)]

    if not df.empty:
        df = df.sort_values(by='Title', key=lambda col: col.str.lower())

    books = df.to_dict(orient='records')
    return render_template('index.html', books=books, query=search_query, field=search_field)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    """Individual book detail page"""
    df = get_books_data()
    
    if df.empty or book_id < 1 or book_id > len(df):
        abort(404)
    
    # Sort by title to maintain consistent indexing
    df = df.sort_values(by='Title', key=lambda col: col.str.lower())
    books = df.to_dict(orient='records')
    
    try:
        book = books[book_id - 1]  # Convert to 0-based index
        return render_template('book.html', book=book)
    except IndexError:
        abort(404)

@app.errorhandler(404)
def not_found_error(error):
    """Custom 404 error page"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page"""
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True, port=5002)