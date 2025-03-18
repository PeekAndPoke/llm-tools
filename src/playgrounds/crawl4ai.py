import time

import requests


# For unsecured instances
def test_crawl4ai_async():
    api_token = "crawl4a-local-key"  # Same token set in CRAWL4AI_API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}

    base_url = "http://localhost:11235"

    # Health check
    health = requests.get(f"{base_url}/health")
    print("Health check:", health.json())

    # Basic crawl
    response = requests.post(
        f"{base_url}/crawl",
        headers=headers,
        json={
            "urls": "https://www.nbcnews.com/business",
            "priority": 10
        },
    )

    print("Crawl response:", response.json())

    task_id = response.json()["task_id"]
    print("Task ID:", task_id)

    timeout: int = 300
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Task {task_id} timeout")

        result = requests.get(
            url=f"{base_url}/task/{task_id}",
            headers=headers,
        )
        status = result.json()

        print("Task status:", status)

        if status["status"] == "completed":
            return status

        time.sleep(2)
