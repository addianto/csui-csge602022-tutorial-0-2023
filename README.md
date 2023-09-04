# Tutorial 0

Name: Rickey Astley

StudentID: 2206123456

Class: PBP International

Hobby: Not giving up

Major: Software Design

## Notes

For those who want to be able to use password-based authentication while performing `git push`,
you can create a personal access token and use it as a password during `git push`.
Follow these steps to create the token:

1. Open GitHub.com.
2. Go to your account settings - Developer Settings.
3. Choose Personal access tokens - Tokens (classic).
4. Generate a new token (classic).
5. Give it a name, e.g. PBP or any name you prefer.
6. Set the expiration to a reasonable period or select 'No expiration'.
7. Enable all repo scopes.
8. Click "Generate token."
9. Copy the generated token to a secure location. DO NOT SHARE IT AND ENSURE THE TOKEN IS NOT STORED IN ANY GIT REPOSITORY!
10. Try performing `git push` from your local repository again, and use the token as the password.

Alternatively, you can follow the recommended authentication suggested by GitHub. That is, by using SSH-based authentication. It is more secure and more aligned with the best practices in the industry.
