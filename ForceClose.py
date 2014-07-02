import sublime, sublime_plugin

class ForceCloseViewCommand(sublime_plugin.WindowCommand):
    def run(self, group = -1, index = -1):
        '''Force closes a view.

        If the view has an underlying file, it is saved, then closed. If it doesn't, the file is cleared then closed. Losing all progress.
        If either the view group or index is not specified, the active view is used.'''

        # TODO: check if the file_name is known but the file itself is missing. Meaning, Sublime Text has saved it at one point but the
        #       underlying file is now AWOL. Right now, like Sublime Text's default implementation, the file is resaved in the "missing" location.

        if group == -1 or index == -1:
            the_view = self.window.active_view()
            group, index = self.window.get_view_index(the_view)
        else:
            the_view = next((view for view in self.window.views_in_group(group) if self.window.get_view_index(view) == (group, index)), None)

        if the_view != None:
            file_name = the_view.file_name()
            if file_name == None:
                the_view.set_scratch(True)
            else:
                the_view.run_command('save')
            self.window.run_command('close_by_index', {"group": group, "index": index})
