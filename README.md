# get-github-python
This is a very simple program that asks the user for a GitHub username and returns the name and amount of repositories he/she/they has/have.
1. Gets user input for username (Example: mavhawk64)
2. Using _requests_ and _re_, it sends a GET request to _https://api.github.com/users/username_ where the _username_ is the input username.
3. Finds the _"public_repos":#_ and returns the number using regex and removing the pre-string.
4. Finds the _"name":"a-zA-Z"_ and returns the full name of the user, again using regex and removing the substring.
5. Gets today's date and time using _datetime_.
6. Formats the date and time to be DD Month, YYYY at HH:MM:SS
7. Print results of form: Maverick has 10 repositories posted to GitHub as of 06 April, 2021 at 12:18:50.
