from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="PocketSmart AI")
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>PocketSmart AI</title>
    </head>

    <body>

        <h1>💰 PocketSmart AI</h1>

        <p>Your Smart Budget & Recommendation Assistant</p>

        <h2>Choose a Planner</h2>

        <p>
            <a href="/home-planner">
                <button>🏠 Home Planner</button>
            </a>
        </p>

        <p>
            <a href="/party-planner">
                <button>🎉 Party Planner</button>
            </a>
        </p>

        <p>
            <a href="/jewelry-planner">
                <button>💎 Jewelry Planner</button>
            </a>
        </p>

    </body>
    </html>
    """
@app.get("/home-planner", response_class=HTMLResponse)
def home_planner():
    return """
    <html>

    <head>
        <title>Home Budget Planner</title>
    </head>

    <body>

        <h1>🏠 Home Interior Budget Planner</h1>

        <form action="/generate-home" method="post">

            <label>Total Budget:</label>
            <br>

            <input
                type="number"
                name="budget"
                placeholder="Enter your budget"
                min="1"
                required
            >

            <br><br>

            <label>Room Type:</label>
            <br>

            <select name="room" required>
                <option value="Living Room">Living Room</option>
                <option value="Bedroom">Bedroom</option>
                <option value="Kitchen">Kitchen</option>
                <option value="Dining Room">Dining Room</option>
            </select>

            <br><br>

            <label>Style:</label>
            <br>

            <select name="style" required>
                <option value="Modern">Modern</option>
                <option value="Traditional">Traditional</option>
                <option value="Minimalist">Minimalist</option>
                <option value="Luxury">Luxury</option>
            </select>

            <br><br>

            <button type="submit">
                Generate Recommendations
            </button>

        </form>

        <br>

        <a href="/">
            <button>← Back to Home</button>
        </a>

    </body>

    </html>
    """
@app.post("/generate-home", response_class=HTMLResponse)
def generate_home(
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form(...)
):

    lighting = budget * 0.10
    furniture = budget * 0.50
    wall_decor = budget * 0.20
    decorative_items = budget * 0.20

    return f"""
    <html>

    <head>
        <title>Home Recommendations</title>
    </head>

    <body>

        <h1>🏠 Home Recommendations</h1>

        <h2>Your Details</h2>

        <p><strong>Budget:</strong> ₹{budget:,.2f}</p>

        <p><strong>Room:</strong> {room}</p>

        <p><strong>Style:</strong> {style}</p>

        <hr>

        <h2>💡 Recommended Budget</h2>

        <ul>
            <li>💡 Lighting — ₹{lighting:,.2f}</li>

            <li>🪑 Furniture — ₹{furniture:,.2f}</li>

            <li>🖼️ Wall Decor — ₹{wall_decor:,.2f}</li>

            <li>🪴 Decorative Items — ₹{decorative_items:,.2f}</li>
        </ul>

        <h3>Total Budget: ₹{budget:,.2f}</h3>

        <p>✅ Recommendation is within your budget.</p>

        <br>

        <a href="/home-planner">
            <button>← Plan Again</button>
        </a>

        <a href="/">
            <button>Home</button>
        </a>

    </body>

    </html>
    """
@app.get("/party-planner", response_class=HTMLResponse)
def party_planner():
    return """
    <html>
    <head>
        <title>Party Planner</title>
    </head>

    <body>
        <h1>🎉 Party Budget Planner</h1>

        <form action="/generate-party" method="post">

            <label>Total Budget:</label>
            <br>
            <input type="number" name="budget" required>

            <br><br>

            <label>Number of Guests:</label>
            <br>
            <input type="number" name="guests" required>

            <br><br>

            <label>Event Type:</label>
            <br>

            <select name="event_type">
                <option>Birthday</option>
                <option>Wedding</option>
                <option>Anniversary</option>
                <option>House Party</option>
            </select>

            <br><br>

            <label>Venue:</label>
            <br>

            <input type="text" name="venue" placeholder="Enter venue">

            <br><br>

            <button type="submit">
                Generate Party Plan
            </button>

        </form>

        <br>

        <a href="/">
            <button>← Back</button>
        </a>

    </body>
    </html>
    """


@app.post("/generate-party", response_class=HTMLResponse)
def generate_party(
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...),
    venue: str = Form(...)
):

    catering = budget * 0.40
    decoration = budget * 0.20
    entertainment = budget * 0.20
    venue_cost = budget * 0.20

    return f"""
    <html>

    <head>
        <title>Party Recommendations</title>
    </head>

    <body>

        <h1>🎉 Party Plan</h1>

        <h2>Your Details</h2>

        <p><strong>Budget:</strong> ₹{budget:,.2f}</p>
        <p><strong>Guests:</strong> {guests}</p>
        <p><strong>Event:</strong> {event_type}</p>
        <p><strong>Venue:</strong> {venue}</p>

        <hr>

        <h2>💰 Budget Allocation</h2>

        <ul>
            <li>🍽️ Catering — ₹{catering:,.2f}</li>
            <li>🎈 Decoration — ₹{decoration:,.2f}</li>
            <li>🎵 Entertainment — ₹{entertainment:,.2f}</li>
            <li>🏛️ Venue — ₹{venue_cost:,.2f}</li>
        </ul>

        <h3>Total Budget: ₹{budget:,.2f}</h3>

        <p>✅ Your party plan is within your budget.</p>

        <br>

        <a href="/party-planner">
            <button>← Plan Again</button>
        </a>

        <a href="/">
            <button>Home</button>
        </a>

    </body>

    </html>
    """
@app.get("/jewelry-planner", response_class=HTMLResponse)
def jewelry_planner():
    return """
    <html>

    <head>
        <title>Jewelry Planner</title>
    </head>

    <body>

        <h1>💎 Jewelry Budget Planner</h1>

        <form action="/generate-jewelry" method="post">

            <label>Budget:</label>
            <br>
            <input
                type="number"
                name="budget"
                placeholder="Enter your budget"
                required
            >

            <br><br>

            <label>Occasion:</label>
            <br>

            <select name="occasion">
                <option>Wedding</option>
                <option>Party</option>
                <option>Birthday</option>
                <option>Festival</option>
                <option>Daily Wear</option>
            </select>

            <br><br>

            <label>Style:</label>
            <br>

            <select name="style">
                <option>Traditional</option>
                <option>Modern</option>
                <option>Minimalist</option>
                <option>Luxury</option>
            </select>

            <br><br>

            <label>Jewelry Type:</label>
            <br>

            <select name="jewelry_type">
                <option>Necklace</option>
                <option>Earrings</option>
                <option>Bangles</option>
                <option>Ring</option>
                <option>Complete Set</option>
            </select>

            <br><br>

            <button type="submit">
                Generate Jewelry Recommendations
            </button>

        </form>

        <br>

        <a href="/">
            <button>← Back to Home</button>
        </a>

    </body>

    </html>
    """
@app.post("/generate-jewelry", response_class=HTMLResponse)
def generate_jewelry(
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...),
    jewelry_type: str = Form(...)
):

    necklace = budget * 0.40
    earrings = budget * 0.20
    bangles = budget * 0.20
    ring = budget * 0.20

    return f"""
    <html>

    <head>
        <title>Jewelry Recommendations</title>
    </head>

    <body>

        <h1>💎 Jewelry Recommendations</h1>

        <h2>Your Details</h2>

        <p><strong>Budget:</strong> ₹{budget:,.2f}</p>

        <p><strong>Occasion:</strong> {occasion}</p>

        <p><strong>Style:</strong> {style}</p>

        <p><strong>Jewelry Type:</strong> {jewelry_type}</p>

        <hr>

        <h2>✨ Recommended Budget</h2>

        <ul>

            <li>
                💎 Necklace — ₹{necklace:,.2f}
            </li>

            <li>
                👂 Earrings — ₹{earrings:,.2f}
            </li>

            <li>
                💍 Bangles — ₹{bangles:,.2f}
            </li>

            <li>
                💍 Ring — ₹{ring:,.2f}
            </li>

        </ul>

        <h3>
            Total Budget: ₹{budget:,.2f}
        </h3>

        <p>
            ✅ Recommendations are within your budget.
        </p>

        <br>

        <a href="/jewelry-planner">
            <button>← Plan Again</button>
        </a>

        <a href="/">
            <button>Home</button>
        </a>

    </body>

    </html>
    """