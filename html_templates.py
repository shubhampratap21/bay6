css = """
    <style>
        /* Main background of the app */
        body {
            background-color: #1e1e1e; /* Dark grey background */
            color: white; /* White text for readability */
        }

        /* Title (BayMax6) styling */
        h1 {
            color:white; /* Cyan color for the heading */
            font-weight: bold;
        }

        /* Chat container background */
        .st-emotion-cache-janbn0, .st-emotion-cache-4oy321 {
            background-color: #2a2a2a; /* Lighter grey for chat container */
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }

        /* User Chat Message */
        .st-emotion-cache-janbn0 {
            background-color: #222222; /* Grey for user messages */
            color: white;
        }

        /* AI Chat Message */
        .st-emotion-cache-4oy321 {
            background-color: #000000; /* Slightly lighter grey for AI messages */
            color: white;
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e; /* Dark grey sidebar background */
            color: white;
            width: 380px !important;
        }

        /* Buttons in the sidebar */
        button {
            background-color: #444444; /* Grey button background */
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }

        button:hover {
            background-color: #555555; /* Slightly lighter on hover */
        }

        /* Chat input box */
        input[type="text"] {
            background-color: #333333;
            color: white;
            border: 1px solid #555555;
        }

        /* Scrollbar customization */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #1e1e1e;
        }

        ::-webkit-scrollbar-thumb {
            background: #555555;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #666666;
        }
    </style>
"""
