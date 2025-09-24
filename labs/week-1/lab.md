# Week 1 Lab - Teaser


**Goal:**  
Get comfortable calling real APIs. By the end, you’ll be able to request live data from the CoinGecko API using your API key, inspect JSON responses, and practice with tools like Postman or curl.


## ✅ Prerequisites

- A GitHub account + your fork of this repo.
- Laptop with internet access.
- (Optional) VS Code installed if you prefer coding right away.


## 🥅 Steps

### 1. Get Your API Key

1. Go to the [CoinGecko API docs](https://docs.coingecko.com/).
2. Sign up for a free/demo account.
3. Copy your **API key** — you’ll need this for every request.
    - CoinGecko uses a header:
        ```
        x-cg-demo-api-key: YOUR_KEY_HERE
        ```

---

### 2. Sign in to Postman (VS Code) & Install the extension

1. Open VS Code.
2. Go to **Extensions Marketplace** → search for **Postman** → install.
3. **Sign up or log in** with your Postman account inside VS Code.
4. Create a **New HTTP Request**

---

### 3. Start with a simple request

#### 3A) In Postman (VS Code)

- Method: `GET`
- URL:
	```
	https://api.coingecko.com/api/v3/ping
	```
- Headers:
```
x-cg-demo-api-key: YOUR_KEY_HERE
```

#### 3B) With cURL (terminal)

Run this in your terminal:

```bash
curl -X GET "https://api.coingecko.com/api/v3/ping" \
  -H "x-cg-demo-api-key: YOUR_KEY_HERE"
```

You should see a tiny JSON response.

---

### 4. Add query params (markets endpoint)

Now call the **coins/markets** endpoint.

#### 4A) In Postman (VS Code)
- Method: `GET`
- URL (with query params inline):
