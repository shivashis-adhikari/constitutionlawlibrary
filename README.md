# Constitutional Law Library 📚

A simple digital library I built for my dad, Prof. Bipin Adhikari, to help organize and browse his extensive collection of constitutional law books and resources.

## What it does

- Browse through constitutional law books with search functionality
- View detailed information about each book including author, publisher, year, and contents
- Clean, dark-themed interface that's easy on the eyes
- Mobile-friendly design for reading on any device

## How I built it

- **Flask** - Simple Python web framework
- **Pandas** - For handling the book data from Google Sheets
- **TailwindCSS** - For the styling (I'm not great at CSS, so this helped!)
- **Google Sheets** - As the database (keeps it simple for dad to update)

## Running it locally

```bash
pip install -r requirements.txt
python app.py
```

Then visit `http://localhost:5002`

## Deployment

It's deployed on Vercel. Just push to main branch and it updates automatically.

## Why I made this

My dad has collected hundreds of constitutional law books over the years, and finding specific books or topics was becoming difficult. I wanted to create something simple where he could search through his collection digitally, even though he still prefers physical books (of course).

It's not fancy, but it works and makes his research a bit easier. Sometimes the simple solutions are the best ones.

---

Made with ❤️ for the best constitutional law professor I know.