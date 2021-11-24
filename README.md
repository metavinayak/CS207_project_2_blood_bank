# CS207_project_2_blood_bank
<!-- Insert your github ids in parenthesis -->
## Team Details
1. [Pushkar Patel](https://github.com/pushkar-dev)
2. [Vinayak Sachan](https://github.com/metavinayak)
3. [Himakshi Gupta](https://github.com/Himakshi-gupta14)
4. [Aniket Sukhija](https://github.com/Sukhija-Aniket)
5. [Isha Sukhija](https://github.com/isha9943)
6. [Shruti Jain]()
7. [Harsh Kumar]()

Credits for Login feature: https://github.com/Faouzizi/Create_LoginPage.git

## Installation :

Fork and Clone the repository
   ```bash
   git clone <source_url>
   ```
Now cd to the project folder

## Method 1 : Virtual Environment Install

### Setup environment
1. Make a virtual environment
   ```
   virtualenv <directory_name>
    ```
    You may need to install virtualenv first by
    ```
    pip install virtualenv
    ```
2. Activate environment
    ```
    <directory_name>\Scripts\activate
    ```
    for linux
    ```bash
    source <directory_name>/bin/activate
    ```
3. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run Server
    ```bash
    python main.py
    ```
5. Deactivate environment when done
    ```
    deactivate
    ```
Note: Replace <directory_name> with any name

## Method 2 : Global Install

1. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
2. Run Server
    ```bash
    python main.py
    ```
## Method 3 : Docker :

```
sudo docker run -p 5000:5000 --name blood_bank metavinayak/blood_bank:latest
```

Use **Ctrl+C** to exit.

Finally use

```
sudo docker stop blood_bank

sudo docker rm blood_bank
```