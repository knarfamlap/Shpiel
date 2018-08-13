
        user = users.get_current_user()

        if user:
            email_address = user.nickname()
            cssi_user = User.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
            if cssi_user:
                self.response.write('''
                    Welcome %s %s (%s)! <br> %s <br>''' % (
                    cssi_user.first_name,
                    cssi_user.last_name,
                    email_address,
                    signout_link_html))
          # If the user hasn't been to our site, we ask them to sign up
            else:
                pass
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, signout_link_html))
        else:
          self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
              users.create_login_url('/')))

    def post(self):
      user = users.get_current_user()
      if not user:
      # You shouldn't be able to get here without being logged in
        self.error(500)
        return
      cssi_user = CssiUser(
          first_name=self.request.get('first_name'),
          last_name=self.request.get('last_name'),
          id=user.user_id())
      cssi_user.put()
      self.response.write('Thanks for signing up, %s!' %
        cssi_user.first_name)
