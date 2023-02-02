# ATHackathon

## Linux

- create env.sh file
- add the following variables:

  ``` text
  export API_KEY="your api key"
  export USERNAME="sandbox"
  export URL="https://api.sandbox.africastalking.com/version1/messaging"
  export SHORT_CODE="7633"
  ```

  ``` bash
  source env.sh
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

- start the server

 ``` bash
    flask run
 ```

## Windows / Linux (Recommended)

- create .env file in the root directory
- add the following variables:

  ``` text
  API_KEY=your-secret-api-key
  USERNAME=sandbox
  URL=https://api.sandbox.africastalking.com/version1/messaging
  SHORT_CODE=7633
  ```

  ``` shell
  python3 -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

- start server

  ``` shell
  flask run
  ```

  - start server in debug mode (recommended)

  ``` shell
  flask --debug run
  ```
