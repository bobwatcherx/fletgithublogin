import os
from flet import *
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider

def main(page:Page):
	data = Column()
	provider = GitHubOAuthProvider(
		client_id=os.getenv("GITHUB_CLIENT_ID"),
		client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
		redirect_url="http://localhost:8550/api/oauth/redirect"
		)

	# LOGIN FUNCTION HERE
	def login_btn(e):
		page.login(provider,scope=['public_repo'])

	# LISTEN IF LOGIN BUTTON CLICK
	def on_login(e):
		print("access token : " , page.auth.token.access_token)
		print("user id : ",page.auth.user.id)
		print("you name :" , page.auth.user['name'])
		print("Login : " , page.auth.user['login'])
		print("email : " , page.auth.user['email'])
		# IF USER FOUND THEN APPEND TO COLUMN FOR DISPLAY USER
		data.controls.append(
			Column([
				Text(f"username : {page.auth.user['name']}"),
				Text(f"email :  {page.auth.user['email']}"),
				])

			)


		hidebutton()


	# CREATE LOGOUT FUNCTION BUTTON
	def logout_btn(e):
		# IF LOGOUT REMOVE ALL DATA 
		data.controls.clear()
		page.logout()

	# LISTEN IF BUTTON LOGOUT IS CLICK
	def on_logout(e):
		print("YOu logout NOW.....")
		hidebutton()


	# HIDE YOU LOGOUT BUTTON AND LOGIN BUTTON HERE
	def hidebutton():
		# THIS LOGIC IS IF YOU NOT USER IS LOGIN THEN SHOW LOGIN BUTTON
		login_mybutton.visible = page.auth is None
		# THIS LOGIC IS IF USER AFTER LOGIN THEN HIDE LOGIN BUTTON
		logout_mybutton.visible = page.auth is not None
		# CHANGE UPDATE ALL
		page.update()

	# CREATE LOGIN LOGOUT BUTTON ELEVATED
	login_mybutton = ElevatedButton("Login With github",
					color="white",
					bgcolor="green",
					on_click=login_btn
					)
	logout_mybutton = ElevatedButton("Logout",
					color="white",
					bgcolor="red",
					on_click=logout_btn
					)

	# REGISTER YOU LISTEN LOGIN AND LOGOUT HERE
	page.on_login = on_login
	page.on_logout = on_logout

	# NEXT STEP IS CALL HIDEBUTTON FUNCTION ONE
	# FOR DETECT USER IS LOGIN OR LOGOUT
	hidebutton()

	# THEN DESIGN YOU SCREEN HERE

	page.vertical_alignment="center"

	page.add(
		Column([
			Row([
				Container(
					content=Column([
						Text("Please Login NOW ",size=30),
						login_mybutton,
						logout_mybutton,

						# SHOW DATA HERE
						data
						])
					)

				],alignment="center")
			],alignment="center")


		)

flet.app(port=8550,target=main)