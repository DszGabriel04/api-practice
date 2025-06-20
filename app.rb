require 'sinatra'

# Set the public folder to serve static files
set :public_folder, 'static'
set :protection, except: :host_authorization
set :allowed_hosts, ['example.com', 'www.example.com']

# Route for the landing page
get '/' do
  <<-HTML
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>API Practice - Home</title>
      <link rel="stylesheet" href="/style.css">
      <style>
          body {
              background: linear-gradient(120deg, #f8fafc 0%, #e0e7ff 100%);
              min-height: 100vh;
              margin: 0;
              font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
              display: flex;
              align-items: center;
              justify-content: center;
          }
          .landing-container {
              background: #fff;
              padding: 2.5rem 3rem;
              border-radius: 16px;
              box-shadow: 0 6px 32px rgba(0,0,0,0.13);
              text-align: center;
              min-width: 320px;
          }
          h1 {
              margin-bottom: 0.5em;
              color: #2d3a4a;
          }
          .desc {
              color: #5c6b7a;
              margin-bottom: 2em;
          }
          .route-btns {
              display: flex;
              flex-direction: column;
              gap: 1.2em;
              margin-bottom: 1.5em;
          }
          .route-btns button {
              padding: 0.9em 1.5em;
              font-size: 1.1em;
              border: none;
              border-radius: 8px;
              background: #6366f1;
              color: #fff;
              cursor: pointer;
              transition: background 0.18s;
              box-shadow: 0 2px 8px rgba(99,102,241,0.08);
          }
          .route-btns button:hover {
              background: #4338ca;
          }
          .footer {
              color: #a0aec0;
              font-size: 0.95em;
              margin-top: 1.5em;
          }
      </style>
  </head>
  <body>
      <div class="landing-container">
          <h1>API Practice</h1>
          <div class="desc">Welcome! Choose a feature to explore:</div>
          <div class="route-btns">
              <button onclick="window.location.href='/time/london'">World Clock (Sample: London)</button>
              <button onclick="window.location.href='/tictactoe'">Tic Tac Toe Game</button>
              <button onclick="window.location.href='/calculator'">Calculator</button>
              <button onclick="window.location.href='/rps'">Rock Paper Scissors ✊✋✌️</button>
          </div>
          <div class="footer">&copy; 2025 API Practice App</div>
      </div>
  </body>
  </html>
  HTML
end

# Define additional routes for your static files if needed
get '/tictactoe' do
  redirect '/tictactoe.html'
end

get '/calculator' do
  redirect '/calculator.html'
end

get '/rps' do
  redirect '/rps.html'
end

# Start the server
run! if app_file == $0
