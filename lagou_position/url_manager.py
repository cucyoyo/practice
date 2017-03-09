
class UrlManager(object):

    def __init__ (self):
        self.new_ids = set()
        self.old_ids = set()

    def add_new_id(self, id):
       if id is None:
           return
       if id not in self.new_ids and id not in self.old_ids:
           self.new_ids.add(id)

    def add_new_ids(self, ids):
        if ids is None or len(ids) == 0:
            return
        for id in ids:
            self.add_new_id(id)

    def has_new_id(self):
        return len(self.new_ids) != 0

    def get_new_id(self):
        new_id = self.new_ids.pop()
        self.old_ids.add(new_id)
        return new_id

