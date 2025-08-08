from cocoAPI.cocoLog import cocoLog
from cocoAPI.cocoGet import cocoGet
from cocoAPI.cocoSearch import cocoSearch
from cocoAPI.cocoAdvSearch import cocoAdvSearch


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
      self.get = cocoGet(self._cocoLog)
      self.search = cocoSearch(self._cocoLog)
      self.advSearch = cocoAdvSearch(self._cocoLog)
