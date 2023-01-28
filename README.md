# ATHackathon

- create env.sh file
- add the following values:

  ``` text
  export API_KEY="your api key"
  export USERNAME="sandbox"
  export URL="https://api.sandbox.africastalking.com/version1/messaging"
  export SHORT_CODE="7633"
  ```

  ``` bash
    source env.sh
    pip install -r requirements.txt
  ```

- start the server

 ``` bash
    flask run --debugger
 ```
