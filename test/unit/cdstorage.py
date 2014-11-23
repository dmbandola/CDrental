class CDStorage(object):
    def __init__(self):
        self.cds = {}

    def add_cd(self, cd):
        self.cds[cd.cd_id] = cd

    def get_cd_info(self, cd_id):
        return self.cds.get(cd_id)
  
