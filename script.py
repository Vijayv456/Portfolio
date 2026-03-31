import requests, json

query = {
    "query": """query userProfile($username: String!) {
        matchedUser(username: $username) {
            profile { ranking reputation userAvatar }
            submitStats { acSubmissionNum { difficulty count } }
        }
    }""",
    "variables": {"username": "Vijay4vtv"}
}

res = requests.post("https://leetcode.com/graphql", json=query)

with open("data1.json", "w") as f:
    json.dump(res.json(), f)