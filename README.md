# Booking Party Bot - A Chatbot Integrated with Custom Data and OpenAI API

Booking Party Bot is a chatbot that leverages custom data and the OpenAI API to provide interactive and dynamic conversations.

## Getting Started

Follow the steps below to set up and run the Booking Party Bot on your local machine.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (version specified in requirements.txt)
- Git

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nguyenvoankhoa/BookingPartyBot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BookingPartyBot
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Obtain your API_KEY and ASSISTANT_ID from the OpenAI API.

2. Create a `.env` file in the project root and add the following lines:

    ```env
    API_KEY=your_openai_api_key
    ASSISTANT_ID=your_openai_assistant_id
    ```

    Replace `your_openai_api_key` and `your_openai_assistant_id` with your actual OpenAI API key and assistant ID.

## Usage

Run the Booking Party Bot using the following command:

```bash
python app.py

