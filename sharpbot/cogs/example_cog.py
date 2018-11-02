#  import tags
#
#  Importing tags allows you to use the bot from other files.
#
#  Make sure your cogs are placed in the 'Cogs' Folder, or else it will not
#  be loaded.
#
#  To add changes to the bot, use the !restart command, it will re-load all
#  the code.
#
#
#  @tags.tag(" This is where you put your infomation about the command.")
#  def test_command(self):
#      self.message("Hello, this is a test.")
#
#
#    This will send the the message when you type !test_command to the bot in
#    messenger. Remember, the command is automatically added to the !commands
#    list.
#
#  You can also take the "client" instance into your own code, allowing you to
#  use the functionality of the fbchat module in your code.
#
#   class test_class():
#       def __init__(self, client):
#           self.client = client
#
#       def threads(self):
#           threads = self.client.fetchThreadList()
#           return threads
#
#   @tags.tag():
#   def threads(self):
#		"""
#		Get a threads list"
#		"""
#
#       test = test_class(self.bot())      ---> self.bot() passes the client.
#       self.message(test.threads())
#
#
#
