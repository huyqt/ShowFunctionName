import sublime, sublime_plugin

class ShowFunctionNameCommand(sublime_plugin.TextCommand):
	def run(self, pt):
		view = self.view

		# initiate the fuction name to an empty string
		function_name = ""

		# get the current ptr and count backwards
		for ptr in reversed(range(view.sel()[0].b)):

			current_region = view.word(ptr)
			current_word = view.substr(current_region)
			word_scope_name = view.scope_name(ptr)

			# if the scope name contains "name.function"
			# we found it, save off the word and break
			if word_scope_name.find("name.function") != -1:
				function_name = current_word
				break

		# set the status bar to the current function
		view.set_status('FunctionName', function_name)
