from cocoAPI.cocoLog import cocoLog
from cocoAPI.cocoMol import cocoMol
from cocoAPI.cocoOrg import cocoOrg
from cocoAPI.cocoSearch import cocoSearch
from cocoAPI.cocoCollect import cocoCollect

class cocoPy:
   def __init__(
                self,
                email,
                password
                ):
      # create login instance
      self._cocoLog = cocoLog()
      self._cocoLog.login(
                          email = email,
                          password = password
                          )

      self.mol = cocoMol(self._cocoLog)
      self.org = cocoOrg(self._cocoLog)
      self.search = cocoSearch(self._cocoLog)
      self.collect = cocoCollect(self._cocoLog)
