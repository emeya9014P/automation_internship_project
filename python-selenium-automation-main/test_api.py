import requests

print("=== Starting API Tests ===")

# 1. GET Request (Read User List)
get_url = "https://reqres.in/api/users?page=2"
get_response = requests.get(get_url)

assert get_response.status_code == 200, f"Expected 200, got {get_response.status_code}"
get_data = get_response.json()
assert get_data["page"] == 2
print(f"✅ GET Test Passed! (Page: {get_data['page']}, Users: {len(get_data['data'])})")


# 2. POST Request (Create User)
post_url = "https://reqres.in/api/users"
payload = {
    "name": "Eme",
    "job": "QA Automation Engineer"
}

post_response = requests.post(post_url, json=payload)

assert post_response.status_code == 201, f"Expected 201, got {post_response.status_code}"
post_data = post_response.json()
assert post_data["name"] == "Eme"
print(f"✅ POST Test Passed! (User ID: {post_data['id']}, Name: {post_data['name']})")


# 3. PUT Request (Update User)
put_url = "https://reqres.in/api/users/2"
put_payload = {
    "name": "Eme",
    "job": "Senior QA Automation Engineer"
}

put_response = requests.put(put_url, json=put_payload)

assert put_response.status_code == 200, f"Expected 200, got {put_response.status_code}"
put_data = put_response.json()
assert put_data["job"] == "Senior QA Automation Engineer"
print(f"✅ PUT Test Passed! (Updated Job: {put_data['job']})")


# 4. DELETE Request (Delete User)
delete_url = "https://reqres.in/api/users/2"
delete_response = requests.delete(delete_url)

assert delete_response.status_code == 204, f"Expected 204, got {delete_response.status_code}"
print(f"✅ DELETE Test Passed! (Status Code: {delete_response.status_code})")

print("=== All API Tests Completed Successfully ===")