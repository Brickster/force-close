from os.path import exists

import sublime, sublime_plugin

class ForceCloseViewCommand(sublime_plugin.WindowCommand):

    def run(self, group = -1, index = -1):
        '''Force closes a view.

        If the view has an underlying file, it is saved, then closed. If it doesn't, the file is cleared then closed. Losing all progress.
        If either the view group or index is not specified, the active view is used.'''

        if group == -1 or index == -1:
            the_view = self.window.active_view()
            group, index = self.window.get_view_index(the_view)
        else:
            the_view = next((view for view in self.window.views_in_group(group) if self.window.get_view_index(view) == (group, index)), None)

        if the_view != None:

            settings = sublime.load_settings('force_close.sublime-settings')

            has_file = the_view.file_name() != None
            should_save = the_view.is_dirty() and has_file and settings.get('save_when_possible')
            is_orphan = has_file and not exists(the_view.file_name())

            if (should_save and not is_orphan) or (is_orphan and settings.get('save_orphaned_views')):
                the_view.run_command('save')
            else:
                the_view.set_scratch(True)

            self.window.run_command('close_by_index', {"group": group, "index": index})
